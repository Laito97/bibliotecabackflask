from app.models.model_prestamo import Prestamo
import pandas as pd

class RecomendacionesService:
    @staticmethod
    def cargar_datos_entrenamiento():
        try:
            print("[INFO] Consultando préstamos con estado 3...")
            prestamos = Prestamo.query.all()

            data = []
            for prestamo in prestamos:
                if (
                    prestamo.prestamo_estado_id == 3 and
                    prestamo.usuario_solicita is not None and
                    prestamo.libro is not None
                ):
                    data.append({
                        "usuario_id": prestamo.usuario_solicita.usuario_id,
                        "libro_id": prestamo.libro.libro_id
                    })

            df = pd.DataFrame(data)
            print("[INFO] DataFrame creado:", df.shape)
            return df

        except Exception as e:
            print("[ERROR] al cargar datos de entrenamiento:")
            import traceback
            traceback.print_exc()
            return pd.DataFrame()
