const fs = require("fs");
const xml2js = require("xml2js");
const https = require("https");

const url = "https://meteo.arso.gov.si/uploads/probase/www/observ/surface/text/sl/observation_LJUBL-ANA_BEZIGRAD_latest.xml";

https.get(url, (res) => {
    const path = `${__dirname}/tmp.xml`;
    const filePath = fs.createWriteStream(path);
    res.pipe(filePath);
    filePath.on("finish", () => {
        filePath.close();
        const parser = new xml2js.Parser();
        fs.readFile(path, "utf8", function (err, data) {
            if (err) {
                console.log("Err1111");
                console.log(err);
                return;
            }
            parser.parseString(data.replace(/&(?!(?:apos|quot|[gl]t|amp);|#)/g, "&amp;"), function (err, result) {
                if (err) {
                    console.log("Err");
                    console.log(err);
                    return;
                }
                console.log(result.data.metData[0].t_degreesC[0]);
                console.log(result.data.metData[0].nn_shortText[0]);
                console.log(result.data.metData[0].tsUpdated[0]);
            });
        });
    })
})
