from pydantic_settings import BaseSettings
from pydantic import SecretStr
        
        
# * создаем класс для определения url базы данных
class DatabaseConfig(BaseSettings):
    HOST : SecretStr
    PORT : SecretStr
    USER : SecretStr
    PASSWORD : SecretStr
    DATABASE : SecretStr
    
    class Config:
        # * указываем корневой путь из каталога с исполняемым файлом
        env_file = 'database/.config'
        env_file_encoding = 'utf-8'

# * создаем объект класса, которые будем испортировать в другие файлы
database_config = DatabaseConfig()