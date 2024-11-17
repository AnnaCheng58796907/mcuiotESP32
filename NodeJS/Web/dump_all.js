function dump_data(content) {
  process.stdout.write(content)
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