from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier.components.prepare_base_model import PrepareBaseModel
from cnnClassifier import logger

STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config1 = ConfigurationManager()
        data_ingestion_config = config1.get_data_ingestion_config()
        data_ingestion = DataIngestion(config = data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

        # print("stage 2 started") 

        config2 = ConfigurationManager()
        prepare_base_model_config = config2.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()



if __name__ == "__main__":
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
    



# STAGE_NAME = "Prepare base model"


# class PrepareBaseModelTrainingPipeline:
#     def __init__(self):
#         pass

#     def main(self):
#         config = ConfigurationManager()
#         prepare_base_model_config = config.get_prepare_base_model_config()
#         prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
#         prepare_base_model.get_base_model()
#         prepare_base_model.update_base_model()



# if __name__ == '__main__':
#     try:
#         logger.info(f"*******************")
#         logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
#         obj = PrepareBaseModelTrainingPipeline()
#         obj.main()
#         logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
#     except Exception as e:
#         logger.exception(e)
#         raise e