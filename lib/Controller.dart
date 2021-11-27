import 'dart:io';
import 'package:http/http.dart' as http;
import 'package:path/path.dart';
import 'dart:async';

asyncFileUpload(String text, File file) async{
  //create multipart request for POST or PATCH method
  var request = http.MultipartRequest("POST", Uri.parse("http://10.1.248.11:80/image"));
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
}