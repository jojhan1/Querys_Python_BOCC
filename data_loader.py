import pandas as pd
import time  # Para medir el tiempo de carga (opcional)
import asyncio
import nest_asyncio
from playwright.async_api import async_playwright
import requests
from bs4 import BeautifulSoup

def cargar_base_datos(ruta):
    print("Iniciando la carga del archivo 'base_final_s.csv'... Por favor, espera.")
    
    try:
        # Medir el tiempo de carga (opcional)
        inicio = time.time()
        
        # Cargar el archivo CSV
        base = pd.read_csv(ruta, sep='|', engine='c', low_memory=False)
        
        # Tiempo transcurrido (opcional)
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
        global df
        async with async_playwright() as playwright:
            df = await download_csv_excel_from_divipola(playwright)
            print(df.head())
        return df
    
    return asyncio.run(main())

if __name__ == "__main__":
    # Ruta al archivo
    ruta_archivo = '../01_Datos/base_final_s.csv'

    # Ejecutar la carga
    base = cargar_base_datos(ruta_archivo)
    
    # Verificar si se cargó correctamente
    if base is not None:
        print("\nLa carga del archivo base_final_s.csv se realizó con éxito.")
    else:
        print("No se puede proceder porque la carga falló.")

    # Ejecutar la carga de DIVIPOLA
    df_divipola = cargar_divipola()
    print(df_divipola.head())
