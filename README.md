# 🦛 Happy Hipo

Tu calculadora amiga para comprar casa sin sustos 🏡✨

Happy Hipo es una aplicación web interactiva construida con Streamlit que te ayuda a calcular todos los costes asociados a la compra de una vivienda, incluyendo gastos de comisión, impuestos, y simulaciones de financiación.

## 🌟 Características

- **💰 Cálculo de Costes Totales**: Desglose completo de todos los gastos
  - Precio del piso
  - Comisión inmobiliaria + IVA (21%)
  - ITP (Impuesto de Transmisiones Patrimoniales: 5.4%)
  - Costes fijos de tasación y notaría (2.500€)

- **🏦 Escenarios de Financiación**: Tabla con la entrada necesaria para diferentes porcentajes de hipoteca
  - 95%, 90%, 85% y 80%
  - Cálculo automático de entrada requerida
  - Visualización clara del porcentaje de financiación actual

- **📅 Calculadora de Cuota Mensual**: Simula tu cuota hipotecaria
  - TAE personalizable (por defecto 2.5%)
  - Plazo ajustable (por defecto 30 años)
  - Cálculo de intereses totales
  - Recomendación de ingresos mensuales (cuota máxima 35%)

## 🚀 Instalación

### Requisitos previos
- Python 3.8 o superior
- pip

### Pasos de instalación

1. Clona este repositorio:
```bash
git clone https://github.com/elenaosknowmad/piso_utils.git
cd piso_utils
```

2. Crea un entorno virtual (recomendado):
```bash
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## 🎯 Uso

Ejecuta la aplicación con:

```bash
streamlit run pisocalculator.py
```

La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`

### Parámetros de entrada

- **Precio del Piso**: Precio base de la vivienda
- **Comisión Inmobiliaria**: Porcentaje de comisión (por defecto 3.5%)
- **Entrada**: Cantidad inicial que aportas (por defecto 42.000€)

## 📊 Pestañas de la aplicación

### 1. 💰 Costes Totales
Visualiza el desglose completo de todos los gastos asociados a la compra.

### 2. 🏦 Escenarios de Financiación
Compara diferentes opciones de financiación y descubre cuánta entrada necesitas para cada porcentaje de hipoteca.

### 3. 📅 Cuota Mensual
Calcula tu cuota mensual ajustando el TAE y el plazo de la hipoteca.

## 🛠️ Tecnologías

- **Streamlit**: Framework para crear aplicaciones web interactivas
- **Pandas**: Manipulación y análisis de datos
- **Python**: Lenguaje de programación

## 📝 Ejemplo de uso

```python
# La aplicación calcula automáticamente:
# - Costes adicionales al precio del piso
# - Porcentaje de hipoteca sobre el precio
# - Cuota mensual con amortización francesa
# - Intereses totales a pagar
```

## 🎨 Características del diseño

- Interfaz minimalista y elegante
- Diseño responsive
- Organización por pestañas para mejor UX
- Alertas contextuales según el porcentaje de financiación
- Formato de moneda español (€)

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo LICENSE para más detalles.

## 👥 Autores

- Elena - [@elenaosknowmad](https://github.com/elenaosknowmad)

## 🙏 Agradecimientos

- Streamlit por el increíble framework
- La comunidad de Python por las herramientas

---

Hecho con ❤️ y 🦛 por Happy Hipo
