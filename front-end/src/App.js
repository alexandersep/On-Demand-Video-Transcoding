import './App.css';

function App() {
  let displayImageCheck = false;

  //returns URL to display image
  function transcodeImage(mediaName, mediaScale, mediaEncoding, mediaNameOutput){
    let imageBLOB;
    fetch('http://127.0.0.1:4000/transcoder', {
      method: 'POST',
      body: JSON.stringify({
        "mediaName": mediaName,
        "mediaScale": mediaScale,
        "mediaEncoding": mediaEncoding,
        "mediaNameOutput": mediaNameOutput,
      }),
      headers: {
        'Content-Type': 'application/json'
      }
    }).then((res) => res.json())
    .then((blob) => {
      let binaryData = [];
      binaryData.push(blob)
      imageBLOB = new Blob(binaryData);
    }).catch((err) =>{
      console.log(err.message);
    });

    return URL.createObjectURL(imageBLOB);
  }

  function imageShown(){
    console.log("WORKS!")
    displayImageCheck = true;
  }

  function displayImage(condition){
    if(!condition){
      return <h1>Error: Image not found!</h1>
    }
    else {
      return  <img src={transcodeImage("house.jpg", "640:480", "H264", "house-downscaled.jpg")} alt="The transcoded result."/>
    }
  }

  return (
    <div className="App">
      <button className="transcode-button" onClick={imageShown()}>Transcode Image</button>
      {displayImage(displayImageCheck)}
    </div>
  );
}

export default App;
