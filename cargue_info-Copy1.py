{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d9f1b67c-adc1-4dd2-8846-429a502675b0",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bda59cab-2f2a-499f-b63d-5eb3c3d83ead",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "826be6ee-e493-4ddf-a8ba-86ac12396caa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Iniciando la carga del archivo 'base_final_s.csv'... Por favor, espera.\n",
      "Carga completada exitosamente en 37.99 segundos.\n",
      "Dimensiones del DataFrame: (5340181, 24)\n",
      "\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import time  # Para medir el tiempo de carga (opcional)\n",
    "\n",
    "def cargar_base_datos(ruta):\n",
    "    print(\"Iniciando la carga del archivo 'base_final_s.csv'... Por favor, espera.\")\n",
    "    \n",
    "    try:\n",
    "        # Medir el tiempo de carga (opcional)\n",
    "        inicio = time.time()\n",
    "        \n",
    "        # Cargar el archivo CSV\n",
    "        base = pd.read_csv(ruta, sep='|', engine='c', low_memory=False)\n",
    "        \n",
    "        # Tiempo transcurrido (opcional)\n",
    "        fin = time.time()\n",
    "        tiempo_carga = fin - inicio\n",
    "        \n",
    "        print(f\"Carga completada exitosamente en {tiempo_carga:.2f} segundos.\")\n",
    "        print(f\"Dimensiones del DataFrame: {base.shape}\")\n",
    "        return base\n",
    "    \n",
    "    except FileNotFoundError:\n",
    "        print(\"ERROR: No se pudo cargar el archivo. El archivo 'base_final_s.csv' no se encuentra en la ruta especificada.\")\n",
    "        return None\n",
    "    except pd.errors.EmptyDataError:\n",
    "        print(\"ERROR: No se pudo cargar el archivo. El archivo 'base_final_s.csv' está vacío.\")\n",
    "        return None\n",
    "    except pd.errors.ParserError:\n",
    "        print(\"ERROR: No se pudo cargar el archivo. Hay un problema con el formato del CSV (separador o estructura).\")\n",
    "        return None\n",
    "    except MemoryError:\n",
    "        print(\"ERROR: No se pudo cargar el archivo. El archivo es demasiado grande para la memoria disponible.\")\n",
    "        return None\n",
    "    except Exception as e:\n",
    "        print(f\"ERROR: No se pudo cargar el archivo. Detalle del error: {str(e)}\")\n",
    "        return None\n",
    "\n",
    "# Ruta al archivo\n",
    "ruta_archivo = '../01_Datos/base_final_s.csv'\n",
    "\n",
    "# Ejecutar la carga\n",
    "base = cargar_base_datos(ruta_archivo)\n",
    "\n",
    "# Verificar si se cargó correctamente\n",
    "if base is not None:\n",
    "    print(\"\")\n",
    "    \n",
    "else:\n",
    "    print(\"No se puede proceder porque la carga falló.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e0a961fb-320c-4d23-ba4e-dfafe99214ad",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "043a01de-0109-4b17-b563-4c794f477567",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   Código Departamento Nombre Departamento  Código Municipio Nombre Municipio  \\\n",
      "0                    5           ANTIOQUIA              5001         MEDELLÍN   \n",
      "1                    5           ANTIOQUIA              5002        ABEJORRAL   \n",
      "2                    5           ANTIOQUIA              5004         ABRIAQUÍ   \n",
      "3                    5           ANTIOQUIA              5021       ALEJANDRÍA   \n",
      "4                    5           ANTIOQUIA              5030            AMAGÁ   \n",
      "\n",
      "  Tipo: Municipio / Isla / Área no municipalizada    longitud   Latitud  \n",
      "0                                       Municipio  -75,581775  6,246631  \n",
      "1                                       Municipio  -75,428739  5,789315  \n",
      "2                                       Municipio  -76,064304  6,632282  \n",
      "3                                       Municipio  -75,141346  6,376061  \n",
      "4                                       Municipio  -75,702188  6,038708  \n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Unnamed: 0</th>\n",
       "      <th>Tipo_Entidad</th>\n",
       "      <th>Nombre_Tipo_Entidad</th>\n",
       "      <th>Codigo_Entidad</th>\n",
       "      <th>Nombre_Entidad</th>\n",
       "      <th>Fecha_Corte</th>\n",
       "      <th>Tipo_de_persona</th>\n",
       "      <th>Sexo</th>\n",
       "      <th>Tamaño_de_empresa</th>\n",
       "      <th>Tipo_de_crédito</th>\n",
       "      <th>...</th>\n",
       "      <th>margen_adicional</th>\n",
       "      <th>Montos_desembolsados</th>\n",
       "      <th>Numero_de_creditos_desembolsados</th>\n",
       "      <th>Grupo_Etnico</th>\n",
       "      <th>Antiguedad_de_la_empresa</th>\n",
       "      <th>Tipo_de_Tasa</th>\n",
       "      <th>Rango_monto_desembolsado</th>\n",
       "      <th>Clase_deudor</th>\n",
       "      <th>Codigo_CIIU</th>\n",
       "      <th>Codigo_Municipio</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>7</td>\n",
       "      <td>1</td>\n",
       "      <td>BC-ESTABLECIMIENTO BANCARIO</td>\n",
       "      <td>39</td>\n",
       "      <td>Banco Davivienda</td>\n",
       "      <td>01/12/2023</td>\n",
       "      <td>Natural</td>\n",
       "      <td>Masculino</td>\n",
       "      <td>Microempresa</td>\n",
       "      <td>Comercial ordinario</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>231,573</td>\n",
       "      <td>6</td>\n",
       "      <td>Sin información (1)</td>\n",
       "      <td>No aplica(1)</td>\n",
       "      <td>FS</td>\n",
       "      <td>Hasta 1 SMLMV</td>\n",
       "      <td>Deudor de la entidad</td>\n",
       "      <td>10.0</td>\n",
       "      <td>17001.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>16</td>\n",
       "      <td>1</td>\n",
       "      <td>BC-ESTABLECIMIENTO BANCARIO</td>\n",
       "      <td>39</td>\n",
       "      <td>Banco Davivienda</td>\n",
       "      <td>08/12/2023</td>\n",
       "      <td>Natural</td>\n",
       "      <td>Masculino</td>\n",
       "      <td>No aplica</td>\n",
       "      <td>Consumo</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>6,697,643.3</td>\n",
       "      <td>1</td>\n",
       "      <td>Sin información (1)</td>\n",
       "      <td>No aplica(1)</td>\n",
       "      <td>FS</td>\n",
       "      <td>Mayor a 5 SMLMV menor o igual a 10 SMLMV</td>\n",
       "      <td>Deudor de la entidad</td>\n",
       "      <td>10.0</td>\n",
       "      <td>68547.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>18</td>\n",
       "      <td>1</td>\n",
       "      <td>BC-ESTABLECIMIENTO BANCARIO</td>\n",
       "      <td>6</td>\n",
       "      <td>Itaú</td>\n",
       "      <td>01/12/2023</td>\n",
       "      <td>Natural</td>\n",
       "      <td>Masculino</td>\n",
       "      <td>No aplica</td>\n",
       "      <td>Consumo</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>13,744,221.05</td>\n",
       "      <td>19</td>\n",
       "      <td>Sin información (1)</td>\n",
       "      <td>No aplica(1)</td>\n",
       "      <td>FS</td>\n",
       "      <td>Mayor a 1 SMLMV menor o igual a 3 SMLMV</td>\n",
       "      <td>Deudor de la entidad</td>\n",
       "      <td>10.0</td>\n",
       "      <td>68001.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>23</td>\n",
       "      <td>1</td>\n",
       "      <td>BC-ESTABLECIMIENTO BANCARIO</td>\n",
       "      <td>53</td>\n",
       "      <td>Banco W S.A.</td>\n",
       "      <td>08/12/2023</td>\n",
       "      <td>Natural</td>\n",
       "      <td>Femenino</td>\n",
       "      <td>Microempresa</td>\n",
       "      <td>Crédito productivo</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1,625,400</td>\n",
       "      <td>1</td>\n",
       "      <td>Sin información (1)</td>\n",
       "      <td>0 a 5 años</td>\n",
       "      <td>FS</td>\n",
       "      <td>Mayor a 1 SMLMV y menor o igual a 2 SMLMV</td>\n",
       "      <td>Deudor nuevo en la entidad</td>\n",
       "      <td>1410.0</td>\n",
       "      <td>41551.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>34</td>\n",
       "      <td>1</td>\n",
       "      <td>BC-ESTABLECIMIENTO BANCARIO</td>\n",
       "      <td>42</td>\n",
       "      <td>Scotiabank Colpatria S.A.</td>\n",
       "      <td>22/12/2023</td>\n",
       "      <td>Natural</td>\n",
       "      <td>Masculino</td>\n",
       "      <td>No aplica</td>\n",
       "      <td>Consumo</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>2,172,362</td>\n",
       "      <td>10</td>\n",
       "      <td>Sin información (1)</td>\n",
       "      <td>No aplica(1)</td>\n",
       "      <td>FS</td>\n",
       "      <td>Mayor a 1 SMLMV menor o igual a 3 SMLMV</td>\n",
       "      <td>Deudor de la entidad</td>\n",
       "      <td>4321.0</td>\n",
       "      <td>13001.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5340176</th>\n",
       "      <td>40814415</td>\n",
       "      <td>1</td>\n",
       "      <td>BC-ESTABLECIMIENTO BANCARIO</td>\n",
       "      <td>30</td>\n",
       "      <td>Banco Caja Social S.A.</td>\n",
       "      <td>22/12/2023</td>\n",
       "      <td>Jurídica</td>\n",
       "      <td>No aplica</td>\n",
       "      <td>Microempresa</td>\n",
       "      <td>Comercial ordinario</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>838,032.11</td>\n",
       "      <td>8</td>\n",
       "      <td>No aplica</td>\n",
       "      <td>No aplica(1)</td>\n",
       "      <td>FS</td>\n",
       "      <td>Hasta 1 SMLMV</td>\n",
       "      <td>Deudor de la entidad</td>\n",
       "      <td>6201.0</td>\n",
       "      <td>68001.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5340177</th>\n",
       "      <td>40814418</td>\n",
       "      <td>4</td>\n",
       "      <td>CF-COMPAÑÍA DE FINANCIAMIENTO</td>\n",
       "      <td>26</td>\n",
       "      <td>Tuya</td>\n",
       "      <td>01/12/2023</td>\n",
       "      <td>Natural</td>\n",
       "      <td>Masculino</td>\n",
       "      <td>No aplica</td>\n",
       "      <td>Consumo</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>17,000</td>\n",
       "      <td>1</td>\n",
       "      <td>Sin información (1)</td>\n",
       "      <td>No aplica(1)</td>\n",
       "      <td>FS</td>\n",
       "      <td>Hasta 1 SMLMV</td>\n",
       "      <td>Deudor de la entidad</td>\n",
       "      <td>81.0</td>\n",
       "      <td>5579.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5340178</th>\n",
       "      <td>40814432</td>\n",
       "      <td>1</td>\n",
       "      <td>BC-ESTABLECIMIENTO BANCARIO</td>\n",
       "      <td>7</td>\n",
       "      <td>Bancolombia</td>\n",
       "      <td>15/12/2023</td>\n",
       "      <td>Jurídica</td>\n",
       "      <td>No aplica</td>\n",
       "      <td>Gran empresa</td>\n",
       "      <td>Comercial ordinario</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1,236,381</td>\n",
       "      <td>6</td>\n",
       "      <td>No aplica</td>\n",
       "      <td>más de 5 y hasta 10 años</td>\n",
       "      <td>FS</td>\n",
       "      <td>Hasta 1 SMLMV</td>\n",
       "      <td>Deudor de la entidad</td>\n",
       "      <td>4651.0</td>\n",
       "      <td>25214.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5340179</th>\n",
       "      <td>40814433</td>\n",
       "      <td>1</td>\n",
       "      <td>BC-ESTABLECIMIENTO BANCARIO</td>\n",
       "      <td>7</td>\n",
       "      <td>Bancolombia</td>\n",
       "      <td>29/12/2023</td>\n",
       "      <td>Natural</td>\n",
       "      <td>Femenino</td>\n",
       "      <td>No aplica</td>\n",
       "      <td>Consumo</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>3,080,000</td>\n",
       "      <td>9</td>\n",
       "      <td>Sin información (1)</td>\n",
       "      <td>No aplica(1)</td>\n",
       "      <td>FS</td>\n",
       "      <td>Hasta 1 SMLMV</td>\n",
       "      <td>Deudor de la entidad</td>\n",
       "      <td>10.0</td>\n",
       "      <td>25785.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5340180</th>\n",
       "      <td>40814437</td>\n",
       "      <td>1</td>\n",
       "      <td>BC-ESTABLECIMIENTO BANCARIO</td>\n",
       "      <td>39</td>\n",
       "      <td>Banco Davivienda</td>\n",
       "      <td>29/12/2023</td>\n",
       "      <td>Natural</td>\n",
       "      <td>Masculino</td>\n",
       "      <td>No aplica</td>\n",
       "      <td>Consumo</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>81,810</td>\n",
       "      <td>1</td>\n",
       "      <td>Sin información (1)</td>\n",
       "      <td>No aplica(1)</td>\n",
       "      <td>FS</td>\n",
       "      <td>Hasta 1 SMLMV</td>\n",
       "      <td>Deudor de la entidad</td>\n",
       "      <td>4645.0</td>\n",
       "      <td>5088.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5340181 rows × 24 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "         Unnamed: 0  Tipo_Entidad            Nombre_Tipo_Entidad  \\\n",
       "0                 7             1    BC-ESTABLECIMIENTO BANCARIO   \n",
       "1                16             1    BC-ESTABLECIMIENTO BANCARIO   \n",
       "2                18             1    BC-ESTABLECIMIENTO BANCARIO   \n",
       "3                23             1    BC-ESTABLECIMIENTO BANCARIO   \n",
       "4                34             1    BC-ESTABLECIMIENTO BANCARIO   \n",
       "...             ...           ...                            ...   \n",
       "5340176    40814415             1    BC-ESTABLECIMIENTO BANCARIO   \n",
       "5340177    40814418             4  CF-COMPAÑÍA DE FINANCIAMIENTO   \n",
       "5340178    40814432             1    BC-ESTABLECIMIENTO BANCARIO   \n",
       "5340179    40814433             1    BC-ESTABLECIMIENTO BANCARIO   \n",
       "5340180    40814437             1    BC-ESTABLECIMIENTO BANCARIO   \n",
       "\n",
       "         Codigo_Entidad             Nombre_Entidad Fecha_Corte  \\\n",
       "0                    39           Banco Davivienda  01/12/2023   \n",
       "1                    39           Banco Davivienda  08/12/2023   \n",
       "2                     6                       Itaú  01/12/2023   \n",
       "3                    53               Banco W S.A.  08/12/2023   \n",
       "4                    42  Scotiabank Colpatria S.A.  22/12/2023   \n",
       "...                 ...                        ...         ...   \n",
       "5340176              30     Banco Caja Social S.A.  22/12/2023   \n",
       "5340177              26                       Tuya  01/12/2023   \n",
       "5340178               7                Bancolombia  15/12/2023   \n",
       "5340179               7                Bancolombia  29/12/2023   \n",
       "5340180              39           Banco Davivienda  29/12/2023   \n",
       "\n",
       "        Tipo_de_persona       Sexo Tamaño_de_empresa      Tipo_de_crédito  \\\n",
       "0               Natural  Masculino      Microempresa  Comercial ordinario   \n",
       "1               Natural  Masculino         No aplica              Consumo   \n",
       "2               Natural  Masculino         No aplica              Consumo   \n",
       "3               Natural   Femenino      Microempresa   Crédito productivo   \n",
       "4               Natural  Masculino         No aplica              Consumo   \n",
       "...                 ...        ...               ...                  ...   \n",
       "5340176        Jurídica  No aplica      Microempresa  Comercial ordinario   \n",
       "5340177         Natural  Masculino         No aplica              Consumo   \n",
       "5340178        Jurídica  No aplica      Gran empresa  Comercial ordinario   \n",
       "5340179         Natural   Femenino         No aplica              Consumo   \n",
       "5340180         Natural  Masculino         No aplica              Consumo   \n",
       "\n",
       "         ... margen_adicional Montos_desembolsados  \\\n",
       "0        ...              0.0              231,573   \n",
       "1        ...              0.0          6,697,643.3   \n",
       "2        ...              0.0        13,744,221.05   \n",
       "3        ...              0.0            1,625,400   \n",
       "4        ...              0.0            2,172,362   \n",
       "...      ...              ...                  ...   \n",
       "5340176  ...              0.0           838,032.11   \n",
       "5340177  ...              0.0               17,000   \n",
       "5340178  ...              0.0            1,236,381   \n",
       "5340179  ...              0.0            3,080,000   \n",
       "5340180  ...              0.0               81,810   \n",
       "\n",
       "        Numero_de_creditos_desembolsados         Grupo_Etnico  \\\n",
       "0                                      6  Sin información (1)   \n",
       "1                                      1  Sin información (1)   \n",
       "2                                     19  Sin información (1)   \n",
       "3                                      1  Sin información (1)   \n",
       "4                                     10  Sin información (1)   \n",
       "...                                  ...                  ...   \n",
       "5340176                                8            No aplica   \n",
       "5340177                                1  Sin información (1)   \n",
       "5340178                                6            No aplica   \n",
       "5340179                                9  Sin información (1)   \n",
       "5340180                                1  Sin información (1)   \n",
       "\n",
       "         Antiguedad_de_la_empresa Tipo_de_Tasa  \\\n",
       "0                    No aplica(1)           FS   \n",
       "1                    No aplica(1)           FS   \n",
       "2                    No aplica(1)           FS   \n",
       "3                      0 a 5 años           FS   \n",
       "4                    No aplica(1)           FS   \n",
       "...                           ...          ...   \n",
       "5340176              No aplica(1)           FS   \n",
       "5340177              No aplica(1)           FS   \n",
       "5340178  más de 5 y hasta 10 años           FS   \n",
       "5340179              No aplica(1)           FS   \n",
       "5340180              No aplica(1)           FS   \n",
       "\n",
       "                          Rango_monto_desembolsado  \\\n",
       "0                                    Hasta 1 SMLMV   \n",
       "1         Mayor a 5 SMLMV menor o igual a 10 SMLMV   \n",
       "2          Mayor a 1 SMLMV menor o igual a 3 SMLMV   \n",
       "3        Mayor a 1 SMLMV y menor o igual a 2 SMLMV   \n",
       "4          Mayor a 1 SMLMV menor o igual a 3 SMLMV   \n",
       "...                                            ...   \n",
       "5340176                              Hasta 1 SMLMV   \n",
       "5340177                              Hasta 1 SMLMV   \n",
       "5340178                              Hasta 1 SMLMV   \n",
       "5340179                              Hasta 1 SMLMV   \n",
       "5340180                              Hasta 1 SMLMV   \n",
       "\n",
       "                       Clase_deudor Codigo_CIIU Codigo_Municipio  \n",
       "0              Deudor de la entidad        10.0          17001.0  \n",
       "1              Deudor de la entidad        10.0          68547.0  \n",
       "2              Deudor de la entidad        10.0          68001.0  \n",
       "3        Deudor nuevo en la entidad      1410.0          41551.0  \n",
       "4              Deudor de la entidad      4321.0          13001.0  \n",
       "...                             ...         ...              ...  \n",
       "5340176        Deudor de la entidad      6201.0          68001.0  \n",
       "5340177        Deudor de la entidad        81.0           5579.0  \n",
       "5340178        Deudor de la entidad      4651.0          25214.0  \n",
       "5340179        Deudor de la entidad        10.0          25785.0  \n",
       "5340180        Deudor de la entidad      4645.0           5088.0  \n",
       "\n",
       "[5340181 rows x 24 columns]"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import asyncio\n",
    "import nest_asyncio\n",
    "from playwright.async_api import async_playwright\n",
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "import pandas as pd\n",
    "\n",
    "# Cargamos la información necesaria para el procesamiento\n",
    "base = pd.read_csv('../01_Datos/base_final_s.csv', sep='|') #,engine ='c', low_memory=False\n",
    "\n",
    "# Aplicamos nest_asyncio\n",
    "nest_asyncio.apply()\n",
    "\n",
    "async def download_csv_excel_from_divipola(playwright) -> pd.DataFrame:\n",
    "    browser = await playwright.chromium.launch(headless=True)\n",
    "    context = await browser.new_context()\n",
    "    page = await context.new_page()\n",
    "    await page.goto(\"https://www.datos.gov.co/Mapas-Nacionales/DIVIPOLA-C-digos-municipios/gdxc-w37w/about_data\")\n",
    "    \n",
    "    await page.get_by_role(\"button\", name=\"Exportar\").click()\n",
    "    await page.get_by_test_id(\"export-type-select\").locator(\"#selected-text\").click()\n",
    "    await page.get_by_role(\"option\", name=\"CSV para Excel\", exact=True).locator(\"div\").nth(1).click()\n",
    "    \n",
    "    async with page.expect_download() as download_info:\n",
    "        await page.get_by_test_id(\"export-download-button\").click()\n",
    "    download = await download_info.value\n",
    "    \n",
    "    csv_path = await download.path()\n",
    "    df = pd.read_csv(csv_path)\n",
    "    \n",
    "    await context.close()\n",
    "    await browser.close()\n",
    "    \n",
    "    return df\n",
    "\n",
    "async def main():\n",
    "    global df\n",
    "    async with async_playwright() as playwright:\n",
    "        df = await download_csv_excel_from_divipola(playwright)\n",
    "        print(df.head())\n",
    "\n",
    "await main()\n",
    "base"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8fcb7c06-a353-4ab9-a023-d8021fddc6ed",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
