import 'dart:async';
import 'dart:collection';
import 'dart:typed_data';
import 'dart:ui';

import 'package:flutter/material.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';

/*
class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Google Maps Demo',
      home: MapSample(),
    );
  }
}
*/






class MapSample extends StatefulWidget {
  final double initialLat;
  final double initialLong;

  const MapSample( this.initialLat, this.initialLong );

  @override
  State<MapSample> createState() => MapSampleState();
}

class MapSampleState extends State<MapSample> {
  Completer<GoogleMapController> _controller = Completer();


  Set<Marker> _markers = HashSet<Marker>();

  late CameraPosition _kGooglePlex = CameraPosition(
    target: LatLng( widget.initialLat, widget.initialLong),
    zoom: 0.0,
  );



  @override
  Widget build(BuildContext context) {
    _markers.add( Marker(
      markerId: MarkerId('100'),
      position: LatLng( widget.initialLat, widget.initialLong ),
      infoWindow: InfoWindow(
        title: "Finded Location",
        snippet: "latitude: " +
      widget.initialLat.toString() +
          "  Longitude: " + widget.initialLong.toString()

      )
      //infoWindow: InfoWindow(title: 'Roça', snippet: 'Um bom lugar para estar'),
      //icon: Icon( Icons.location_on  );
    ));



    return new Scaffold(
      body: GoogleMap(
        mapType: MapType.hybrid,
        initialCameraPosition: _kGooglePlex,

        onMapCreated: (GoogleMapController controller) {
          _controller.complete(controller);
          controller.showMarkerInfoWindow(MarkerId('100'));
          },
        markers: _markers,
      ),
    );
  }

  Future<void> _goToTheLake() async {

  }
}