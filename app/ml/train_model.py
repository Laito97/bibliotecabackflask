import pandas as pd
from app.models import Prestamo
from app.database import db
from joblib import dump
from collections import defaultdict

def entrenar_modelo():
    # Obtener datos desde la base de datos
    prestamos = Prestamo.query.all()
    print(f"Cantidad de préstamos obtenidos: {len(prestamos)}")

    data = [
        {'usuario_id': p.usuario_solicita_prestamo, 'libro_id': p.libro_id}
        for p in prestamos
    ]
    df = pd.DataFrame(data)
    print("Primeros préstamos:")
    print(df.head())

    # Solo contar una vez cada préstamo de un libro por un usuario
    df = df.drop_duplicates(subset=['usuario_id', 'libro_id'])

    print("Después de eliminar duplicados:")
    print(df.head())

    # Crear la matriz
    user_book_matrix = df.pivot_table(index='usuario_id', columns='libro_id', aggfunc=lambda x: 1, fill_value=0)
    print("Matriz generada:")
    print(user_book_matrix)

    # Guardar matriz como modelo básico
    dump(user_book_matrix, 'app/ml/model.pkl')
    print("✅ Modelo guardado exitosamente.")


#python -m app.ml.train_model
