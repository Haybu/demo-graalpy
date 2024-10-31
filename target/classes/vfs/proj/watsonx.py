from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from ibm_watsonx_ai.foundation_models.utils.enums import ModelTypes, DecodingMethods

from langchain_ibm import WatsonxLLM

from langchain import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain

import warnings
warnings.filterwarning("ignore")

class PyWatsonx:
    def __init__(self):
        self.parameters =    {
                GenParams.MAX_NEW_TOKENS: 100,
                GenParams.MIN_NEW_TOKENS: 1,
                GenParams.DECODING_METHOD: DecodingMethods.SAMPLE,
                GenParams.TEMPERATURE: 0.5,
                GenParams.TOP_K: 50,
                GenParams.TOP_P: 1
            }

    def setWatsonxModel(self, model, api_key, project_id):
        self.llm = WatsonxLLM(
            model_id=model,
            url='https://us-south.ml.cloud.ibm.com',
            apikey=api_key,
            project_id=project_id,
            params=self.parameters,
        )

    def invoke(self, prompt: str):
        return self.llm.invoke(prompt);

polyglot.export_value("PyWatsonx", PyWatsonx)