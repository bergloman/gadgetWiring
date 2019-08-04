"use strict";

const fs = require("fs");
const rq = require("request");

const url = "https://app.qlector.com/api/v1.0/ingestion/datasources";
const user = "404a6db23ba641b58c8d451f504cdac6";
const api_key = "646d7c86002c43f491c9aa7d14a8aef5";
const file_name = "../sensor_state.txt";

function post(data, cb) {
    const options = {
        json: data,
        headers: { Authorization: "Basic " + new Buffer(user + ":" + api_key).toString("base64") },
        method: "POST",
        uri: url
    };
    rq(options, cb);
}

function main() {
    const lines = fs
        .readFileSync(file_name, { encoding: "utf8" })
        .split("\n");

    for (const line of lines) {
        if (line == "") {
            continue;
        }
        const msg = JSON.parse(line);
        msg.ts = Date.now();
        console.log(msg);
        post(msg, (err, _r, b) => {
            if (err) {
                console.log("Error", err);
            } else {
                console.log("Body:", b);
            }
        });
    }
}

/////////////////////////////////////////////////////////////////////////////////

main();
