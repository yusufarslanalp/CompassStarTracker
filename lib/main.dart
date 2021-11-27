import 'dart:async';

import 'package:flutter/material.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';
import 'Map.dart';

import 'dart:io';
import 'PickImage.dart';
import 'Controller.dart';

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

  Future<void> foo2() async {
    File f = await getFromGallery();
    asyncFileUpload("sky", f);
  }

  Future<void> foo3() async {
    File f = await getFromCamera();
    asyncFileUpload("sky", f);
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
          ElevatedButton(onPressed: null, child: Text( "get info" )),
          ElevatedButton(onPressed: foo2, child: Text( "take from galery" )),
          ElevatedButton(onPressed: foo3, child: Text( "take photo" )),
          Image(image: AssetImage( "assets/sky-stars.jpg" ))
        ],
      )),

    );
  }
}
