import 'package:flutter/material.dart';
import 'dart:math';

void main() => runApp(
      MaterialApp(
        home: Scaffold(
          backgroundColor: Colors.blue,
          appBar: AppBar(
            title: Text('Ask Me Anything'),
            backgroundColor: Colors.blueAccent,
          ),
          body: Ama(),
        ),
      ),
    );

class Ama extends StatefulWidget {
  @override
  _AmaState createState() => _AmaState();
}

class _AmaState extends State<Ama> {
  int img = 1;

  @override
  Widget build(BuildContext context) {
    return Center(
      child: FlatButton(
        onPressed: () {
          setState(() {
            img = Random().nextInt(5) + 1;
          });
        },
        child: Image.asset('images/ball$img.png'),
      ),
    );
  }
}
