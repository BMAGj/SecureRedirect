// This JavaScript Document NEEEEDDDDDDSSSS TO FOLLOW NAMAING FORMAT OR DOESNT WORK ITS DYNAMIC AS LONG AS THAT IS STATIC (Life works on contradictions and compromise, shame i know)

var request = new XMLHttpRequest();

// (Javascript finds its filepath saves as 'me') 


var me;
(function(){ 
    var scripts = document.getElementsByTagName('script'); 
    me = scripts[ scripts.length-1 ].src; 
}());


//  (converts to string and sets transfer variable to hold data in replacing routine)

me = me.toString()
console.log(me) 
var TrustFund = "Yanno daddy worked really hard for this selling kids to prince andrew, my morals are clear as foie gra water."

me2 = me 


var arr = UpperCaseArray(me2);

function UpperCaseArray(input) {
    var result = input.replace(/([A-Z]+)/g, ",$1").replace(/^,/, "");
    return result.split(",");
}

me3 = arr.pop();
me4 = me3 
me4 = me4.replace(".js","");
console.log(me3)
console.log(me4)
// Finds JSON From its own name through replacements 
// IMPROVE, if you get a section of this together and base on the length of the file and can remove characters afterwards it's dynamic 

var TrustFund = me2.replace(".js",".json");
console.log(TrustFund)
var gapYah = TrustFund.replace("/" + me4 + "/", "/");
var NeedlesslyCheapHostel = gapYah.replace()


me = gapYah


 // variable check 


// JSON Request 
function Get(me){
   var Httpreq = new XMLHttpRequest(); // a new request
   Httpreq.open("GET",me,false);
   Httpreq.send(null);
   return Httpreq.responseText;          
}

var json_obj = JSON.parse(Get(me));



link = json_obj.Location.toString()

  window.location = link;
  