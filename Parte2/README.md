# **Agente Autónomo de Clusterización con LangChain**

Referencias:
- [langchain_core.language_models.llms.LLM](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.llms.LLM.html)
- [How to create a custom LLM class](https://python.langchain.com/docs/how_to/custom_llm/)
- [ReActSingleInputOutputParser](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.output_parsers.react_single_input.ReActSingleInputOutputParser.html)

## **Cómo correrlo**
Primero, ver los prerrequisitos enunciados en el archivo `../README.md`. Luego,
habiendo instalado las dependencias y estando en el entorno virtual, correr el
siguiente comando en la terminal:
```bash
python clustering_agent.py
```

Esto iniciará el agente autónomo de clusterización. El agente espera que el usuario
ingrese un comando en inglés para realizar la clusterización o el resumen de los
clusters. El comando debe ser ingresado en la terminal y el agente responderá
directamente en la misma terminal. Para finalizar, se puede enviar el comando
`exit` o `quit`.

## **Supuestos asumidos**
* El agente espera los comandos en inglés (`clusterize`, `summarize`).
* La cantidad de clusters está fija en 5 (no la puede pasar el usuario).
* Para hacer la clusterización, el usuario debe escribir una instrucción que tenga
la subpalabra "clusteriz".
* Para hacer la descripción, el usuario debe escribir una instrucción que tenga
la subpalabra "summariz".

## **Interpretación de la respuesta del agente**
Ante el pedido de clusterización, el agente devuelve el mensaje:
```bash
✅ Clusterized data into 5 groups and saved to iris_data_challenge_with_clusters.csv
```
indicando que la clusterización fue exitosa y que los datos fueron guardados en el
archivo `iris_data_challenge_with_clusters.csv`.

Ante el pedido de resumen, el agente devuelve un mensaje en donde incluye la
cantidad de clusters y el tamaño de cada uno, junto con sus características
normlizadas (TODO: volver a las características originales).

## **Diagrama de flujo de interacción entre usuario, agente y herramientas**
En esta carpeta, se adjunta el archivo `diagrama_agente_clusterizacion.png` que
muestra el flujo de interacción entre el usuario, el agente y las herramientas
utilizadas.

Los mensajes sobre las flechas no son exactamente los de la implementación, sino que
sirven para ilustrar el flujo de información.

Para el comando "summarize", el flujo es similar. Solamente se utiliza otra herramienta
y los mensajes son distintos.