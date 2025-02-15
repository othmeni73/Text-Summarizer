from textSummarizer.components.training import ModelTrainer
from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.logging import logger

class TrainingPipeline:
    def __init__self():
        pass
    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()