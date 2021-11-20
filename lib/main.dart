import 'dart:async';

import 'package:flutter/material.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';
import 'Map.dart';

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

  void foo(){}

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
          ElevatedButton(onPressed: foo, child: Text( "11111111" )),
          ElevatedButton(onPressed: foo, child: Text( "11111111" )),
          ElevatedButton(onPressed: null, child: Text( "11111111" ))
        ],
      )),

    );
  }
}
