// Environment variables - AZURE_STORAGE_ACCOUNT and AZURE_STORAGE_ACCESS_KEY or AZURE_STORAGE_CONNECTION_STRING

const azure = require("azure-storage");
const path = require("path");

class StorageWrapper {

    constructor(containerName) {
        this.blobService = azure.createBlobService();
        this.containerName = containerName;
    }

    createContainer() {
        return new Promise((resolve, reject) => {
            this.blobService.createContainerIfNotExists(this.containerName, { publicAccessLevel: 'blob' }, err => {
                if (err) {
                    reject(err);
                } else {
                    resolve({ message: `Container '${this.containerName}' created` });
                }
            });
        });
    }

    uploadLocalFile(filePath) {
        return new Promise((resolve, reject) => {
            const fullPath = path.resolve(filePath);
            const blobName = path.basename(filePath);
            this.blobService.createBlockBlobFromLocalFile(this.containerName, blobName, fullPath, err => {
                if (err) {
                    reject(err);
                } else {
                    resolve({ message: `Local file "${filePath}" is uploaded` });
                }
            });
        });
    }

    uploadString(blobName, text) {
        return new Promise((resolve, reject) => {
            this.blobService.createBlockBlobFromText(this.containerName, blobName, text, err => {
                if (err) {
                    reject(err);
                } else {
                    resolve({ message: `Text "${text}" is written to blob storage` });
                }
            });
        });
    }

    listContainers() {
        return new Promise((resolve, reject) => {
            this.blobService.listContainersSegmented(null, (err, data) => {
                if (err) {
                    reject(err);
                } else {
                    resolve({ message: `${data.entries.length} containers`, containers: data.entries });
                }
            });
        });
    }
}

module.exports = StorageWrapper;
