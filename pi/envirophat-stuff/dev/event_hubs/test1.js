const { EventHubClient, EventPosition } = require("@azure/event-hubs");
const lr = require("line-reader");

//const inputChunks = [];

// const name = process.env["EVENTHUB_NAME"];
// const cs = process.env["EVENTHUB_CONNECTION_STRING"];

const name = "carvic-test1-eh";
const cs = "Endpoint=sb://carvic-eh-ns-demo.servicebus.windows.net/;SharedAccessKeyName=asa-policy-demo;SharedAccessKey=1mlmiPu9JU3fmEADieTqSBxbVpJCRTEv1QaamD2UtjE=;EntityPath=carvic-test1-eh";
const client = EventHubClient.createFromConnectionString(cs, name);

console.log(new Date(), "------ starting job");

async function sendMsg(body) {
    const data = { body: body }; // { ts: new Date(), val: Math.random() }
    await client.send(data);
    console.log("Message sent successfully.");
}

lr.eachLine(process.stdin, (line, last) => {
    console.log("Received line", line);
    const parts = line.split("=");
    const data = {
        data_source: parts[0],
        ts: new Date(),
        val: +parts[1]
    };
    sendMsg(data)
        .then(async () => {
            //console.log("Done sending line", line);
            if (last) {
                console.log(new Date(), "------ finished");
                process.exit(0);
            }
        })
        .catch(err => {
            console.log(err);
        });
});


// function main() {
//     process.stdin.resume();
//     process.stdin.setEncoding("utf8");

//     process.stdin.on("data", function (chunk) {
//         inputChunks.push(chunk);
//     });

//     process.stdin.on("end", function () {
//         const parsedData = JSON.parse(inputChunks.join());

//         sendMsg(parsedData).catch((err) => {
//             console.log(err);
//         });
//     });
// }

// main(); 
