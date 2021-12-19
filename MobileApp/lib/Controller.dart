import 'dart:io';
import 'package:http/http.dart' as http;
import 'package:path/path.dart';
import 'dart:async';
import 'dart:convert';

class Cordinate{
  double lat;
  double longi;
  
  Cordinate( this.lat, this.longi ){}
  
  @override
  String toString() {
    // TODO: implement toString
    return "lat: " + lat.toString() + "  longi: " + longi.toString();
  }
}

Future<Cordinate>
asyncFileUpload(String text, File file) async{
  //create multipart request for POST or PATCH method
  var request = http.MultipartRequest("POST", Uri.parse("http://192.168.1.70:80/image"));
  //add text fields
  request.fields["image124"] = text;
  //create multipart using filepath, string or bytes
  print( basename( file.path) );
  var pic = await http.MultipartFile.fromPath("file_field", file.path);

  //add multipart to request
  request.files.add(pic);
  var response = await request.send();

  //Get the response from the server
  var responseData = await response.stream.toBytes();
  var responseString = String.fromCharCodes(responseData);
  print(responseString);

  Map<String, dynamic> map = jsonDecode( responseString ); // import 'dart:convert';

  double lat = map['lat'];
  double longi = map['longi'];

  print( lat );
  print( longi );

  return Cordinate(lat, longi);
}