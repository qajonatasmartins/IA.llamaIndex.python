from llama_index.core import Settings
from llama_index.llms.groq import Groq

import os
llm = Groq(model='llama-3.3-70b-versatile',
           api_key= os.environ.get("GROQ_API_KEY")
           )

def calcular_imposto_renda(rendimento:float)->str:
    """"
    Calcula o imposto de renda com base no rendimento anual.
    Args:
        rendimento (float): Rendimento anual do individuo.

    Returns:
        str: O valor do imposto devido com base no rendimento
    """
    if rendimento <= 2000:
        return "Voce está isento de pagar imposto de renda"
    elif 2000< rendimento <=5000:
        imposto = (rendimento-2000)*0.10
        return f"O imposto devido é de R$ {imposto:.2f}, base em um rendimento de R$ {rendimento:.2f}"
    elif 5000 < rendimento <=10000:
        imposto = (rendimento -5000)*0.15+300
        return f"O imposto devido é de R$ {imposto:.2f}, base em um redimento de R$ {rendimento:.2f}"
    else:
        imposto = (rendimento -10000)*0.20+1050
        return f"O imposto devido é de R$ {imposto:.2f}, base em um redimento de R$ {rendimento:.2f}"

### Convertendo função em ferramenta

from llama_index.core.tools import FunctionTool

ferramenta_imposto_renda = FunctionTool.from_defaults(
    fn=calcular_imposto_renda,
    name="Calcular Imposto de Renda",
    description=(
        "Calcular o imposto de renda com base no rendimento anual."
        "Argumento: rendimento (float)"
        "Retorna o valor do imposto devido de acordo com faixas de rendimento."
    )
)

from llama_index.core.agent import FunctionCallingAgentWorker

agent_worker_imposto = FunctionCallingAgentWorker.from_tools(
    tools=[ferramenta_imposto_renda]
)

