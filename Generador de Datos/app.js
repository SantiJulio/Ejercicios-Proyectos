let BD_EXPEDIENTES = []; // Base de datos en memoria para procesar filtros

document.addEventListener("DOMContentLoaded", () => {
    fetch("datos_judiciales_completos.json")
        .then(response => {
            if (!response.ok) throw new Error("No se pudo cargar el dataset.");
            return response.json();
        })
        .then(data => {
            BD_EXPEDIENTES = data;
            ejecutarFiltros(); // Render inicial
            
            // Escuchar el filtro por Fuero
            document.getElementById("filtroFuero").addEventListener("change", ejecutarFiltros);
            
            // Escuchar el buscador por número de expediente
            document.getElementById("buscadorExp").addEventListener("input", ejecutarFiltros);
        })
        .catch(error => console.error("Error inicializando el motor de gestión:", error));
});

// Función centralizada para aplicar filtros combinados (Fuero + Buscador)
function ejecutarFiltros() {
    const fueroSeleccionado = document.getElementById("filtroFuero").value;
    const busqueda = document.getElementById("buscadorExp").value.trim();
    
    let datosFiltrados = BD_EXPEDIENTES;
    
    // 1. Filtrar por fuero
    if (fueroSeleccionado !== "TODOS") {
        datosFiltrados = datosFiltrados.filter(exp => exp.Fuero === fueroSeleccionado);
    }
    
    // 2. Filtrar por buscador de expediente
    if (busqueda !== "") {
        datosFiltrados = datosFiltrados.filter(exp => exp.Nro_Expediente.includes(busqueda));
    }
    
    // Renderizar componentes con los datos procesados en cascada
    procesarYRenderizarMetricas(datosFiltrados);
    renderizarTabla(datosFiltrados); // Llamada corregida
}

function procesarYRenderizarMetricas(expedientes) {
    const total = expedientes.length;
    const tramite = expedientes.filter(e => e.Estado_Causa === "En Trámite").length;
    const resueltas = expedientes.filter(e => e.Estado_Causa === "Resuelto").length;
    
    const sumaDias = expedientes.reduce((acc, current) => acc + current.Dias_Activo, 0);
    const promedioDias = total > 0 ? (sumaDias / total).toFixed(1) : 0;

    document.getElementById("kpi-total").textContent = total.toLocaleString();
    document.getElementById("kpi-tramite").textContent = tramite.toLocaleString();
    document.getElementById("kpi-resueltas").textContent = resueltas.toLocaleString();
    document.getElementById("kpi-dias").textContent = `${promedioDias} días`;

    // Gráfico de Fueros (Verde)
    const conteoFueros = {};
    expedientes.forEach(e => { conteoFueros[e.Fuero] = (conteoFueros[e.Fuero] || 0) + 1; });
    renderizarBarrasFlex(conteoFueros, "chartFuero", " expedientes");

    // Gráfico de Procesos (Azul)
    const sumaDiasProceso = {};
    const conteoProceso = {};
    expedientes.forEach(e => {
        sumaDiasProceso[e.Tipo_Proceso] = (sumaDiasProceso[e.Tipo_Proceso] || 0) + e.Dias_Activo;
        conteoProceso[e.Tipo_Proceso] = (conteoProceso[e.Tipo_Proceso] || 0) + 1;
    });

    const promediosProceso = {};
    Object.keys(conteoProceso).forEach(p => {
        promediosProceso[p] = parseFloat((sumaDiasProceso[p] / conteoProceso[p]).toFixed(1));
    });
    renderizarBarrasFlex(promediosProceso, "chartProceso", " días");
}

// Renderizar las barras analíticas con estilos inyectados de forma segura
function renderizarBarrasFlex(datos, contenedorId, sufijo) {
    const contenedor = document.getElementById(contenedorId);
    if (!contenedor) return;
    contenedor.innerHTML = "";

    const elementos = Object.entries(datos).sort((a, b) => b[1] - a[1]);
    const valorMaximo = Math.max(...elementos.map(item => item[1]), 0);

    const gradienteAzul = "linear-gradient(90deg, #0284c7, #38bdf8)";
    const gradienteVerde = "linear-gradient(90deg, #059669, #34d399)";
    const colorGradiente = contenedorId === "chartFuero" ? gradienteVerde : gradienteAzul;

    elementos.forEach(([clave, valor]) => {
        const porcentaje = valorMaximo > 0 ? (valor / valorMaximo) * 100 : 0;
        
        contenedor.innerHTML += `
            <div class="fila-grafico" style="display: flex; flex-direction: column; gap: 0.4rem; margin-bottom: 1.2rem;">
                <div class="info-grafico" style="display: flex; justify-content: space-between; font-size: 0.9rem; color: #f8fafc; font-weight: 500;">
                    <span class="nombre-etiqueta" style="color: #94a3b8;">${clave}</span>
                    <span class="valor-metrica"><strong>${valor.toLocaleString()}</strong>${sufijo}</span>
                </div>
                <div class="contenedor-progreso" style="background-color: #475569; width: 100%; height: 14px; border-radius: 20px; overflow: hidden; position: relative;">
                    <div class="barra-relleno" style="width: ${porcentaje}%; height: 100%; display: block; border-radius: 20px; transition: width 0.8s ease-in-out; background: ${colorGradiente} !important;"></div>
                </div>
            </div>
        `;
    });
}

// Renderizar listado tabular de causas abajo
function renderizarTabla(expedientes) {
    const cuerpo = document.getElementById("cuerpoTabla");
    if (!cuerpo) return;
    cuerpo.innerHTML = "";
    
    const muestra = expedientes.slice(0, 50); 
    
    if (muestra.length === 0) {
        cuerpo.innerHTML = `<tr><td colspan="7" style="text-align:center; color:#94a3b8;">No se encontraron expedientes con los filtros aplicados.</td></tr>`;
        return;
    }

    muestra.forEach(exp => {
        const fila = document.createElement("tr");
        fila.innerHTML = `
            <td><strong>${exp.Nro_Expediente}</strong></td>
            <td>${exp.Fuero}</td>
            <td>${exp.Juzgado_Radicacion}</td>
            <td>${exp.Tipo_Proceso}</td>
            <td>${exp.Fecha_Inicio}</td>
            <td><span style="color: ${exp.Estado_Causa === 'Resuelto' ? '#34d399' : '#fbbf24'}">${exp.Estado_Causa}</span></td>
            <td>
                <button class="btn-tabla" onclick="cambiarEstadoExpediente('${exp.Nro_Expediente}')">⚙️ Alternar Estado</button>
            </td>
        `;
        cuerpo.appendChild(fila);
    });
}

// Modificación interactiva del estado del expediente en caliente
window.cambiarEstadoExpediente = function(nroExpediente) {
    const index = BD_EXPEDIENTES.findIndex(exp => exp.Nro_Expediente === nroExpediente);
    
    if (index !== -1) {
        const estadoActual = BD_EXPEDIENTES[index].Estado_Causa;
        BD_EXPEDIENTES[index].Estado_Causa = estadoActual === "En Trámite" ? "Resuelto" : "En Trámite";
        ejecutarFiltros();
    }
}