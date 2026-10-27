from abc import ABC, abstractmethod
class CloudStorage(ABC):
    @abstractmethod
    def upload_file(self, filename): pass
    @abstractmethod
    def download_file(self, filename): pass
    @abstractmethod
    def delete_file(self, filename): pass
class DriveStorage(CloudStorage):
    def upload_file(self, filename): print("Uploaded", filename, "to Drive")
    def download_file(self, filename): print("Downloaded", filename, "from Drive")
    def delete_file(self, filename): print("Deleted", filename, "from Drive")
class LocalCloudStorage(CloudStorage):
    def upload_file(self, filename): print("Uploaded", filename, "to local cloud")
    def download_file(self, filename): print("Downloaded", filename, "from local cloud")
    def delete_file(self, filename): print("Deleted", filename, "from local cloud")
for storage in [DriveStorage(), LocalCloudStorage()]:
    storage.upload_file("notes.pdf")
    storage.download_file("notes.pdf")
    storage.delete_file("notes.pdf")
