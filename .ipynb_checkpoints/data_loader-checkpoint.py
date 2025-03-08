# cargar_datos.py
import pandas as pd
import time
import asyncio
import nest_asyncio
from playwright.async_api import async_playwright

def cargar_base_datos():
    """
    Carga un archivo CSV pesado desde una ruta predefinida y muestra mensajes de progreso o error.
    
    Returns:
        pd.DataFrame o None: DataFrame cargado o None si falla.
    """
    ruta = '../01_Datos/base_final_s.csv'  # Ruta fija dentro de la función
    print("Iniciando la carga del archivo 'base_final_s.csv'... Por favor, espera.")
    
    try:
        inicio = time.time()
        base = pd.read_csv(ruta, sep='|', engine='c', low_memory=False)
        fin = time.time()
        tiempo_carga = fin - inicio
        
        print(f"Carga completada exitosamente en {tiempo_carga:.2f} segundos.")
        print(f"Dimensiones del DataFrame: {base.shape}")
        return base
    
    except FileNotFoundError:
        print("ERROR: No se pudo cargar el archivo. El archivo 'base_final_s.csv' no se encuentra en la ruta especificada.")
        return None
    except pd.errors.EmptyDataError:
        print("ERROR: No se pudo cargar el archivo. El archivo 'base_final_s.csv' está vacío.")
        return None
    except pd.errors.ParserError:
        print("ERROR: No se pudo cargar el archivo. Hay un problema con el formato del CSV (separador o estructura).")
        return None
    except MemoryError:
        print("ERROR: No se pudo cargar el archivo. El archivo es demasiado grande para la memoria disponible.")
        return None
    except Exception as e:
        print(f"ERROR: No se pudo cargar el archivo. Detalle del error: {str(e)}")
        return None

def cargar_divipola():
    """
    Descarga y carga el archivo CSV de DIVIPOLA desde datos.gov.co.
    
    Returns:
        pd.DataFrame: DataFrame con los datos de DIVIPOLA.
    """
    nest_asyncio.apply()
    
    async def download_csv_excel_from_divipola(playwright) -> pd.DataFrame:
        browser = await playwright.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto("https://www.datos.gov.co/Mapas-Nacionales/DIVIPOLA-C-digos-municipios/gdxc-w37w/about_data")
        await page.get_by_role("button", name="Exportar").click()
        await page.get_by_test_id("export-type-select").locator("#selected-text").click()
        await page.get_by_role("option", name="CSV para Excel", exact=True).locator("div").nth(1).click()
        
        async with page.expect_download() as download_info:
            await page.get_by_test_id("export-download-button").click()
        download = await download_info.value
        csv_path = await download.path()
        df = pd.read_csv(csv_path)
        
        await context.close()
        await browser.close()
        return df
    
    async def main():
        async with async_playwright() as playwright:
            df = await download_csv_excel_from_divipola(playwright)
            return df
    
    return asyncio.run(main())

# Bloque de ejecución solo si se corre como script principal
if __name__ == "__main__":
    # Ejecutar la carga de base_final_s.csv
    base = cargar_base_datos()
    if base is not None:
        print("\nLa carga del archivo base_final_s.csv se realizó con éxito.")
    else:
        print("No se puede proceder porque la carga falló.")
    
    # Ejecutar la carga de DIVIPOLA
    df_divipola = cargar_divipola()