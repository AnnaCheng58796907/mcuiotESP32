function dump_data(content) {
  //process.stdout.write(content)
 
  var info = JSON.parse(content)
  console.log()
  //console.log(info)
  console.log(info.count)
  //console.log(info.data)
  console.log(info.data[1])
  console.log(info.data[5])
  console.log(info.data[5].stationName)

}

const https = require('https')

const options = {
  hostname: 'wic.heo.taipei',
  port: 443,
  path: '/OpenData/API/Water/Get?stationNo=&loginId=river&dataKey=9E2648AA',
  method: 'GET'
}

const req = https.request(options, res => {
  console.log(`statusCode: ${res.statusCode}`)
  res.on('data', content => {
    dump_data(content)
  })
})

req.end()