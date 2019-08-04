//////////////////////////////////////////////////////////////////////////////////////
// This file is used for testing/mocking purposes.
//////////////////////////////////////////////////////////////////////////////////////

// set these variables before(!) importing the function code
process.env.TEST = "true";
process.env.DESTINATION_MOBILE_NUMS = "+38641234567,+1245677443";

// ok, now import the code
const lib = require("./index");

const context = {
    log: console.log,
    res: null,
    done: () => {
        console.log("Done.");
        console.log(context.res);
    }
};

lib(
    context,
    {
        body: {
            "type": "telemetry",
            "ts": "2019-05-21T00:02:12Z",
            "location": "kolektor-beta",
            "statuses": [
                { "name": "start-gui-server", "status": 0 }
            ]
        }
    })
    .catch(x => {
        console.log("ERROR", x)
    });
