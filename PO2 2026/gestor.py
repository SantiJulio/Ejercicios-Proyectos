from datetime import datetime
from werkzeug.security import check_password_hash
from modelo import db, Organizador, Evaluador, Trabajo, Asignacion

class gestorCongreso:
    def crearBD(self):
        db.create_all()

    def registrarUsuario(self, xt, xr, xa, xap, xn, xe, xarchivo):
        nuevo_trabajo = Trabajo(
            titulo = xt,
            resumen = xr, 
            area = xa, 
            autor_nombre = xn, 
            autor_apellido = xap, 
            autor_email = xe, 
            estado = 'Pendiente',
            archivo_nombre = xarchivo, 
            fecha_envio = datetime.now()
        )
        db.session.add(nuevo_trabajo)
        db.session.commit()
        return nuevo_trabajo.id

    def buscarxIDyCorreo(self,xi,xe):
        return Trabajo.query.filter_by(id = xi, autor_email = xe).first()
           
    def asignarEvaluadoresAutomatico(self):
        trabajos_pendientes = Trabajo.query.filter_by(estado='Pendiente').all()
        cant_asignaciones_realizadas = 0

        for trabajo in trabajos_pendientes:
            # Lista los ID de los evaluadores que ya estan vinculados a esta investigacion
            evaluadores_actuales = [a.evaluador_id for a in trabajo.asignaciones]
            cupos_necesarios = 3 - len(evaluadores_actuales)

            # Solo intentamos asignar si al trabajo aun le faltan evaluadores
            if cupos_necesarios > 0:
                # Busca evaluadores que compartan la misma especialidad tematica del articulo
                evaluadores_area = Evaluador.query.filter_by(area=trabajo.area).all()
                i = 0
                limite_evaluadores = len(evaluadores_area)
                while cupos_necesarios > 0 and i < limite_evaluadores:
                    evaluador = evaluadores_area[i]
                    no_esta_asignado = evaluador.id not in evaluadores_actuales
                    tiene_cupo_disponible = len(evaluador.asignaciones) < evaluador.max_trabajos
                    if no_esta_asignado and tiene_cupo_disponible:
                        nueva_asignacion = Asignacion(
                            trabajo_id=trabajo.id,
                            evaluador_id=evaluador.id
                        )
                        db.session.add(nueva_asignacion)                        
                        evaluadores_actuales.append(evaluador.id)
                        cupos_necesarios -= 1
                        cant_asignaciones_realizadas += 1
                    else:
                        i += 1
        db.session.commit()
        return cant_asignaciones_realizadas
    
    def autenticarOrganizador(self, correo_ingresado, clave_ingresada):
        organizador = Organizador.query.filter_by(correo=correo_ingresado).first()       
        if organizador:
            if organizador.clave == clave_ingresada or check_password_hash(organizador.clave, clave_ingresada):
                return organizador
        return None
    
    def autenticarEvaluador(self, correo_ingresado, clave_ingresada):
        evaluador = Evaluador.query.filter_by(correo=correo_ingresado).first()       
        if evaluador:
            if evaluador.clave == clave_ingresada or check_password_hash(evaluador.clave, clave_ingresada):
                return evaluador               
        return None

    def obtenerAsignacionesEvaluador(self,xid):
        return Asignacion.query.filter_by(evaluador_id=xid)        