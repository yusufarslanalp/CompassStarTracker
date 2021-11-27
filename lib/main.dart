import 'dart:async';

import 'package:flutter/material.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';
import 'Map.dart';

import 'dart:io';
import 'package:http/http.dart' as http;
import 'package:flutter/services.dart' show ByteData, rootBundle;
import 'package:path/path.dart';
import 'package:path_provider/path_provider.dart';
import 'package:image_picker/image_picker.dart';


_asyncFileUpload(String text, File file) async{
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

_getFromGallery() async {
  PickedFile? pickedFile = await ImagePicker().getImage(
    source: ImageSource.gallery,
  );
  if (pickedFile != null) {
    File imageFile = File(pickedFile.path);
    return imageFile;
  }

}

Future<File> getImageFileFromAssets(String path) async {
  final byteData = await rootBundle.load('assets/$path');

  final file = File('${(await getTemporaryDirectory()).path}/$path');
  await file.writeAsBytes(byteData.buffer.asUint8List(byteData.offsetInBytes, byteData.lengthInBytes));

  return file;
}

_getFromCamera() async {
  PickedFile? pickedFile = await ImagePicker().getImage(
    source: ImageSource.camera,
    maxWidth: 1800,
    maxHeight: 1800,
  );
  if (pickedFile != null) {
    File imageFile = File(pickedFile.path);
    return imageFile;
  }
}

void main() => runApp(MyApp());



/// This is the main application widget.
class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  static const String _title = 'Flutter Code Sample';

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      title: _title,
      home: Home(),
    );
  }
}



/// This is the private State class that goes with MyStatefulWidget.
class Home extends StatelessWidget  {
  const Home({Key? key}) : super(key: key);

  Future<void> foo() async {
    //ByteData bytes = await rootBundle.load( 'assets/sky-stars.jpg' );
    //var myFile = File( 'assets/sky-stars.jpg' );
    //print( bytes.lengthInBytes );

    File f = await getImageFileFromAssets( "sky-stars.jpg" );
    _asyncFileUpload("sky", f);

  }

  Future<void> foo2() async {
    File f = await _getFromGallery();
    _asyncFileUpload("sky", f);
  }

  Future<void> foo3() async {
    File f = await _getFromCamera();
    _asyncFileUpload("sky", f);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Sample Code'),
      ),
      body: Center(child: Column(
        crossAxisAlignment: CrossAxisAlignment.center,
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          ElevatedButton(onPressed: foo, child: Text( "send asset" )),
          ElevatedButton(onPressed: foo2, child: Text( "take from galery" )),
          ElevatedButton(onPressed: foo3, child: Text( "take photo" )),
          Image(image: AssetImage( "assets/sky-stars.jpg" ))
        ],
      )),

    );
  }
}
