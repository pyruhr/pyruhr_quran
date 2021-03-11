//webkitURL is deprecated but nevertheless 
URL = window.URL || window.webkitURL;
var gumStream;
//stream from getUserMedia() 
var rec;
//Recorder.js object 
var input;
//MediaStreamAudioSourceNode we'll be recording 
// shim for AudioContext when it's not avb. 
var AudioContext = window.AudioContext || window.webkitAudioContext;
var audioContext = new AudioContext;


function startRecording() {
	/* Simple constraints object, for more advanced audio features see
	https://addpipe.com/blog/audio-constraints-getusermedia/ */

	var constraints = {
	    audio: true,
	    video: false
	} 

	/* We're using the standard promise based getUserMedia()
	https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia */

	navigator.mediaDevices.getUserMedia(constraints).then(function(stream) {
		/* assign to gumStream for later use */
		gumStream = stream;
		/* use the stream */
		input = audioContext.createMediaStreamSource(stream);
		/* Create the Recorder object and configure to record mono sound (1 channel) Recording 2 channels will double the file size */
		rec = new Recorder(input, {
		    numChannels: 1
		}) 
		//start the recording process 
		rec.record()
	})
}

function stopRecording() {
    rec.stop(); //stop microphone access 
    gumStream.getAudioTracks()[0].stop();
    //create the wav blob and pass it on to createDownloadLink 
    rec.exportWAV(upload);
}

// Required for Django CSRF
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
 

// toggle record button
$('#rekam').click(function() {
    $(this).toggleClass("btn btn-danger");
    $(this).toggleClass("btn btn-success btn-round");
    var icon = document.getElementById("icon-rekam");
    var a = icon.firstChild;
    a.data = a.data == "mic_none" ? "stop_circle" : "mic_none";
    var b = icon.nextSibling;
    if (b.data == " Rekam") {
    	b.data = " Stop";
    	startRecording();
    }
    else {
    	b.data = " Rekam";
    	stopRecording();
    }
});


