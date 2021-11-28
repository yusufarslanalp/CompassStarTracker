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

  Future<void> takeFromGalery( context ) async {
    File f = await getFromGallery();
    Cordinate crd = await asyncFileUpload("sky", f);

    Navigator.push(
      context,
      MaterialPageRoute(builder: (context) => MapSample( crd.lat, crd.longi )),
    );
  }

  Future<void> foo3() async {
    File f = await getFromCamera();
    asyncFileUpload("sky", f);
  }

  void goToMap( context, double lat, double long ){
    Navigator.push(
      context,
      MaterialPageRoute(builder: (context) => MapSample( lat, long )),
    );

  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Compass Star Tracker'),
      ),
      body: Container(
        decoration: BoxDecoration(
          image: DecorationImage(
            image: AssetImage("assets/sky-stars.jpg"),
            fit: BoxFit.cover,
          ),
        ),

        child: Center(child: Column(

          crossAxisAlignment: CrossAxisAlignment.center,
          //mainAxisAlignment: MainAxisAlignment.center,
          children: [
            new SizedBox(
              width: 120.0,
              height: 40,
              child: null,
            ),
            Image(image: AssetImage( "assets/logo.jpg" )),
            new SizedBox(
              width: 120.0,
              height: 100,
              child: null,
            ),
            SizedBox(
              width: 140.0,
              child: ElevatedButton(onPressed: () => goToMap( context, 40.8, 29.3 ), child: Text( "get info" ) ),
            ),
            new SizedBox(
              width: 140.0,
              child: ElevatedButton(onPressed: () => takeFromGalery( context ), child: Text( "take from galery" )),
            ),
            new SizedBox(
              width: 140.0,
              child: ElevatedButton(onPressed: foo3, child: Text( "take photo" )),
            )

          ],
        )),
      ),

    );
  }
}
