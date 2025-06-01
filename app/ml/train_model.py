import pandas as pd
from app.models import Prestamo
from app.database import db
from joblib import dump
from collections import defaultdict

def entrenar_modelo():
    # Obtener datos desde la base de datos
    prestamos = Prestamo.query.all()

    data = [
        {'usuario_id': p.usuario_solicita_prestamo, 'libro_id': p.libro_id}
        for p in prestamos
    ]
    df = pd.DataFrame(data)

    # Crear matriz de usuarios y libros
    user_book_matrix = pd.crosstab(df['usuario_id'], df['libro_id'])

    # Guardar matriz como modelo básico
    dump(user_book_matrix, 'app/ml/model.pkl')
    print("Modelo guardado exitosamente.")

if __name__ == '__main__':
    from app import create_app
    app = create_app()
    with app.app_context():
        entrenar_modelo()


#python -m app.ml.train_model
