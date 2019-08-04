const fs = require("fs");
const fsp = fs.promises;
const az = require("./azure_blob_storage");


async function mainAsync() {
    const fileName = "./test.txt";
    const content = JSON.stringify({ ts: Date.now(), status: "ok" });
    await fsp.writeFile(fileName, content, { encoding: "utf8" });

    const containerName = "personal-informer-container";
    const storage = new az(containerName);
    await storage.uploadLocalFile(fileName);
    console.log("done.");
}


mainAsync()
    .catch(err => {
        console.log(err);
    });