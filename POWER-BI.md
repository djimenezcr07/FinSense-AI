# Power BI Desktop: preparación reproducible

No se creó ni verificó un archivo `.pbix`. Power BI Desktop no se utilizó en este entorno. El CSV de FinSense es una exportación real de la cuenta seleccionada; incluye fecha, cuenta, moneda, descripción, tipo, monto positivo, categoría, estado y origen.

1. Abrí FinSense, seleccioná una cuenta y elegí **Informes → Descargar CSV**.
2. En Power BI Desktop gratuito seleccioná **Obtener datos → Texto/CSV** y elegí el archivo. Indicá UTF-8 y coma.
3. En Power Query fijá `fecha` como fecha y `monto` como decimal; el resto como texto. Cargá la tabla con nombre `Movimientos`.
4. Agregá estas medidas DAX:

```DAX
Ingresos = CALCULATE(SUM(Movimientos[monto]), Movimientos[tipo] = "ingreso", Movimientos[estado] = "activo")
Gastos = CALCULATE(SUM(Movimientos[monto]), Movimientos[tipo] = "gasto", Movimientos[estado] = "activo")
Balance neto = [Ingresos] - [Gastos]
```

5. Agregá filtros por cuenta, moneda y fecha. Construí tarjetas de ingresos, gastos y balance; barras de gastos por categoría y una línea mensual.
6. Verificá en la aplicación los totales de la misma cuenta, moneda y período. Nunca combines monedas distintas. Para actualizar, sobrescribí el CSV elegido y seleccioná **Actualizar**; comprobá de nuevo los filtros y totales.

Power BI puede inferir tipos según la configuración regional; revisá explícitamente el separador decimal. La exportación contiene también transacciones anuladas, identificadas en `estado`; las medidas las excluyen. Los campos de texto que comienzan con caracteres de fórmula reciben un apóstrofo de seguridad.
