from textSummary.config.configuration import ConfigurationManager
from textSummary.components.data_validation import DataValidation
from textSummary.logging import logger


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.download_file()
        data_validation.extract_zip_file()