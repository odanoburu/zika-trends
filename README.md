# zika-trends

OBJETIVO: melhorar a alocação de agentes de saúde com base no nível de casos e na tendência epidemiológica (ascendente, descendente, estável) das três doenças, pPE:or bairro e semana epidemiológica.

TARGET_VARIABLE: tendência epidemiológica (ascendente, descendente, estável) das três doenças, por bairro e semana epidemiológica.

ALGORITHM_TYPE: Classification

RELEVANT_DATASETS: casos de dengue+zika+chikun... (clínicos), clima, mapa de ilhas de calor, mapa de uso do solo (meio ambiente), densidade populacional (demográficos), twitter (social media)

HYPOTHESIS: Com os datasets acima conseguimos ao menos prever uma tendência para a semana seguinte, informando a decisão de alocação de pessoal por parte da Secretaria Municipal de Saúde.

PROCESSING_LANGUAGE: Python, QGis LIBRARIES: pandas, numpy, basemap, matplotlib, etc.
