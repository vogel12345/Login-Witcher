import streamlit as st
import pandas as pd
import plotly.express as px
import base64
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_curve, auc, precision_recall_curve
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import os
import json


# Establecer el título de la página
st.set_page_config(page_title='Login - The Witcher 3 Wild Hunt')

# Definir el estilo CSS personalizado para la página
st.markdown("""
    <style>
        /* Establecer el fondo en blanco */
        body {
            background-color: white
        }
        /* Quitar barra */
        .st-emotion-cache-1avcm0n
        {
            visibility: hidden;
        }
        .st-emotion-cache-fis6aj{
            visibility: hidden;
            padding:0;
        }
        .st-emotion-cache-1on073z e1b2p2ww0{
            margin:0;
            padding:0;
        }
    </style>
""", unsafe_allow_html=True)
# Credenciales de usuario para demostración
usuarios = {}

try:
    with open("usuarios.json", "r") as file:
        usuarios = json.load(file)
except FileNotFoundError:
    usuarios = {}

# Página principal
st.title("**Bienvenido a Dashboards STEAM**")
opcion_elegida = st.radio("Selecciona una opción:", ("Iniciar sesión", "Crear cuenta"))

# Función de registro
def register():
    st.subheader("Registro")
    new_use = st.text_input("Ingresa tus Nombre(s)")
    new_ape = st.text_input("Ingresa tus Apellido(s)")
    new_username = st.text_input("Ingresa tu Correo")
    new_password = st.text_input("Ingresa tu Contraseña", type="password")

    if st.button("Registrar"):
        if new_username and new_password:
            if new_username not in usuarios:
                usuarios[new_username] = new_password
                st.success(f"Usuario registrado correctamente: {new_username}")
                st.success(f"Porfavor Regresa a Iniciar Sesión")
                st.success(f"IMPORTANTE: Inicia Sesión con tu Correo y Contraseña")

                # Guarda la información actualizada de los usuarios en el archivo
                with open("usuarios.json", "w") as file:
                    json.dump(usuarios, file)

            else:
                st.error("El usuario ya existe. Por favor, elige otro.")
        else:
            st.warning("Por favor, introduce un usuario y una contraseña.")    

# Función de inicio de sesión
def login():
    st.subheader("Inicio de sesión")
    username = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")

    if st.button("Iniciar sesión"):
        if username in usuarios and usuarios[username] == password:
            st.success(f"Bienvenido, {username}!")
            st.write(f"Puedes ingresar desde el siguiente link:", "[Ir al Dashboard](https://witcher-dash.streamlit.app/)", unsafe_allow_html=True)
            return True
        else:
            st.error("Credenciales incorrectas. Por favor, inténtalo de nuevo.")
            return False

# Mostrar la sección correspondiente según la opción elegida
if opcion_elegida == "Iniciar sesión":
    if login():
        st.write("¡Iniciaste sesión correctamente!")
    
elif opcion_elegida == "Crear cuenta":
    register()
