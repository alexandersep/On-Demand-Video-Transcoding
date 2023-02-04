import './App.css';

function App() {
  // let displayImageCheck = false;

  //returns URL to display image
  function transcodeImage(mediaName, mediaScale, mediaEncoding, mediaNameOutput){
    let imageBLOB;
    fetch('http://127.0.0.1:5000/transcoder', {
      method: 'POST',
      body: JSON.stringify({
        "mediaName": mediaName,
        "mediaScale": mediaScale,
        "mediaEncoding": mediaEncoding,
        "mediaNameOutput": mediaNameOutput,
      })
    }).then((res) => res.json())
    .then((blob) => {
      console.log(blob);
    }).catch((err) =>{
      console.log(err.message);
    });

    return URL.createObjectURL()
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
      {/* <button 
      className="transcode-button" 
      onClick={displayImageCheck = true}
      >Transcode Image</button>
      {displayImage(displayImageCheck)} */}
      <button 
      className="transcode-button" 
      onClick={console.log("WORKS")}
      >Transcode Image</button>
    </div>
  );
}

export default App;
