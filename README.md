# 🧪 Proyecto de Pruebas Web — Selenium + Cypress + QA Tools

## 📘 Contenido
- Selenium (Python + pytest)
- Cypress (JavaScript E2E)
- Instrucciones LoadRunner, ZAP y Hotjar
- Reportes y Plantilla Excel de métricas

## ⚙️ Ejecución
### Selenium
```
python -m venv venv
venv\Scripts\activate
pip install selenium pytest pytest-xdist webdriver-manager pytest-html
pytest selenium_tests -n auto --html=reports/selenium-report.html
```

### Cypress
```
npm install
npx cypress run --spec "cypress/e2e/checkout.spec.js"
```

### OWASP ZAP (Docker)
```
docker run -v %cd%/reports:/zap/reports -t owasp/zap2docker-stable zap-baseline.py -t https://automationpractice.com -r /zap/reports/zap-report.html
```

### LoadRunner
1. Grabar con VuGen el flujo checkout.
2. Configurar 100 Vusers.
3. Analizar resultados con Analysis.

### Hotjar
1. Instalar snippet JS.
2. Configurar heatmaps y recordings.
3. Analizar funnels y scroll depth.

## 📊 Informe de Resultados
Completa la plantilla Excel `informe_calidad.xlsx` en la carpeta `reports/`.
