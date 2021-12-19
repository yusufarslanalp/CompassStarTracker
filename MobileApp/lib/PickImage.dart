import 'dart:io';
import 'package:image_picker/image_picker.dart';

getFromGallery() async {
  PickedFile? pickedFile = await ImagePicker().getImage(
    source: ImageSource.gallery,
  );
  if (pickedFile != null) {
    File imageFile = File( pickedFile.path );
    return imageFile;
  }

}



getFromCamera() async {
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