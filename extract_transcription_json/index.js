const fs = require('fs');
const file6412 = require('./6412548b294e8ad5.json');
const fileabde = require('./abde18308e8c2bac.json');
const request = require('request');

// const sampleUrl = "https://spsvcprodinc.blob.core.windows.net/bestor-948e9f4b-98f0-414a-b695-603be7bddabe/TranscriptionData/c188498a-e92f-4dad-b4ce-f367a3377216_37_0.json?sv=2021-04-10&st=2022-06-09T06%3A17%3A57Z&se=2022-06-09T18%3A22%3A57Z&sr=b&sp=rl&sig=HRDrd%2FXsZT6i52AF%2BdKEk9BJHhnHS4%2F9ScpVznOebWc%3D";


//write data to file
const writeToTextFile = (data, fileName) => {
    fs.writeFile(fileName, data, function (err) {
        if (err) throw err;
        console.log('complete');
    }
    );
}

//append data to file
const appendToTextFile = (data, fileName) => {
    fs.appendFile(fileName, data, function (err) {
        if (err) throw err;
        console.log('complete');
    }
    );
}

//function to get data from URL
const getDataFromUrl = (url) => {
    return new Promise((resolve, reject) => {
        request(url, function (error, response, body) {
            if (error) {
                reject(error);
            }
            resolve(body);
        });
    }
    );
}

//check if the file exists or not in the directory
const isFileExists = (fileName) => {
    if (fs.existsSync(fileName)) {
        return true;
    }
    return false;
}


// let fileName = file6412.values[1].name;
// let url = file6412.values[1].links.contentUrl;
// getDataFromUrl(url).then(data => {
//     writeToTextFile(data, `./6412548b294e8ad5/${fileName}`);
//     console.log(`Completed : ${fileName} \n\n`);
// }
// ).catch(error => {
//     console.log(error);
// });

//get all the urls from the json file
const getUrls = (data) => {
    let urls = [];
    data.values.forEach(transcript => {
        //console.log(transcript);
        //if transcript kind is "Transcription"
        if (transcript.kind == "Transcription") {
            //console.log(transcript.links.contentUrl)
            //appendToTextFile(transcript.links.contentUrl, 'urls.txt');

            //saving the url for each individual transcript
            let url = transcript.links.contentUrl;

            //saving the filename for each individual transcript
            let fileName = transcript.name;

            //saving the url in an array
            urls.push(url);

            //saving the data if the file doesn't exist
            if (!isFileExists(`./abde18308e8c2bac/${fileName}`)) {

                //get the data from the url
                getDataFromUrl(url).then(data => {
                    writeToTextFile(data, `./abde18308e8c2bac/${fileName}`);
                    console.log(`Completed : ${fileName} \n\n`);
                }
                ).catch(error => {
                    console.log(error);
                });

            }
            else {
                let fileName = transcript.name;

                console.log('file already downloaded! : ' + fileName);
            }

        }
    }
    )
    //console.log(urls);
}


//calling the function to get the urls 
getUrls(fileabde);



        // writeToTextFile('hello', 'sheetText.txt');