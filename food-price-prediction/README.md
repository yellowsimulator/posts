## Research questions

Is it possible to predict food price in canada?

What are the factors (variables) that affect food price in canada?

## Solution approach

1 - Collect data and select variables that intuitively or through research might affect food price

2 - Perform an exploratory data analysis to ascertain the causation / correlation between these variables and food price

3 - Chose a machine learning model that best predict food price

4 - train and validate the model


## data organisation

The data follows the medallion architecture :

- bronze contains the raw data
- silver contains the preprocessed data
- gold contaiins the cleaned ans high quality data ready for machine learning


## Some variables to consider

- Weather (Heat wave, drought condition, sever weather: Maybe some sort of average regional temperture)
- Supply chain disruption caused by unforseeing event such as diseases outbreak like covid 19, Russian invasion of Ukrain, natural catastroph, ...
- Pesticide price
- Fertilizer price
- Identify main world producer of certain product, ascess the weather condition in these part of the world
- In which geographical areas are the specific product produced, whats the weather consition there?
- harsh weather condition affect supply amid sustained demand causing price to increase
