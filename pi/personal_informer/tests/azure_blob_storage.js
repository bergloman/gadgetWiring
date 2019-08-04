// Environment variables - AZURE_STORAGE_ACCOUNT and AZURE_STORAGE_ACCESS_KEY or AZURE_STORAGE_CONNECTION_STRING

const azure = require("azure-storage");
// const fs = require("fs");
const path = require("path");

const containerName = "personal-informer-container";
const localFile = "test.txt";

const listContainers = async () => {
    return new Promise((resolve, reject) => {
        blobService.listContainersSegmented(null, (err, data) => {
            if (err) {
                reject(err);
            } else {
                resolve({ message: `${data.entries.length} containers`, containers: data.entries });
            }
        });
    });
};

const createContainer = async (blobService, containerName) => {
    return new Promise((resolve, reject) => {
        blobService.createContainerIfNotExists(containerName, { publicAccessLevel: 'blob' }, err => {
            if (err) {
                reject(err);
            } else {
                resolve({ message: `Container '${containerName}' created` });
            }
        });
    });
};

const uploadString = async (blobService, containerName, blobName, text) => {
    return new Promise((resolve, reject) => {
        blobService.createBlockBlobFromText(containerName, blobName, text, err => {
            if (err) {
                reject(err);
            } else {
                resolve({ message: `Text "${text}" is written to blob storage` });
            }
        });
    });
};

const uploadLocalFile = async (blobService, containerName, filePath) => {
    return new Promise((resolve, reject) => {
        const fullPath = path.resolve(filePath);
        const blobName = path.basename(filePath);
        blobService.createBlockBlobFromLocalFile(containerName, blobName, fullPath, err => {
            if (err) {
                reject(err);
            } else {
                resolve({ message: `Local file "${filePath}" is uploaded` });
            }
        });
    });
};

async function mainAsync() {
    const blobService = azure.createBlobService();
    await createContainer(blobService, containerName);
    const msg = JSON.stringify({ timestamp: "2019-08-03T12:00:00Z", status: "ok" });
    await uploadString(blobService, containerName, "status-coins", msg);
    await uploadLocalFile(blobService, containerName, localFile);
}

mainAsync()
    .catch(err => {
        console.log(err);
    });

// function uploadFile(blobService, localFileName) {
//     console.log("Uploading file", localFileName);
//     blobService.createBlockBlobFromLocalFile(containerName, "taskblob", localFileName, (error, result, response) => {
//         if (error) {
//             console.log(err);
//             return;
//         }
//         console.log("File uploaded", result);
//     });
// }

// function main() {
//     const blobService = azure.createBlobService();
//     blobService.createContainerIfNotExists(containerName, { publicAccessLevel: "blob" }, (error, result, response) => {
//         console.log("createContainerIfNotExists", result);
//         if (error) {
//             console.log(err);
//             return;
//         }
//         uploadFile(blobService, localFile);
//     });
// };


// main();