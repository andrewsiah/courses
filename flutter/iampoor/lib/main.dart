import 'package:flutter/material.dart';

void main() {
  runApp(
    MyApp(),
  );
}

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: "I am Poor :(",
      home: Scaffold(
        appBar: AppBar(
          backgroundColor: Colors.grey[900],
          title: Text('I am super poorrr'),
        ),
        body: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: <Widget>[
            CircleAvatar(
              backgroundImage: NetworkImage(
                "https://picsum.photos/200/200.jpg",
              ),
              radius: 50.0,
            ),
          ],
        ),
      ),
    );
  }
}
