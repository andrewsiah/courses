import 'package:flutter/material.dart';

void main() {
  runApp(
    MyApp(),
  );
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        backgroundColor: Colors.teal,
        body: SafeArea(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget> [
              CircleAvatar(
                radius: 70,
                backgroundImage: AssetImage('images/andrew.jpg',
                ),
              ),
              Text(
                'Andrew Siah',
                style: TextStyle(
                  fontFamily: 'Pacifico',
                  color: Colors.white,
                  fontSize: 40,
                  fontWeight: FontWeight.bold,
                ),
              ),
              Text(
                'Flutter Developer',
                style: TextStyle(
                  fontFamily: 'Montserrat',
                  color: Colors.teal.shade50,
                  fontSize: 20,
                  letterSpacing: 2.5,
                  fontWeight: FontWeight.w300,
                ),
              ),
              SizedBox(
                height: 20.0,
                width: 200,
              child: Divider(
                  color: Colors.teal[100],
              ),
              ),
              Card(
                  margin: EdgeInsets.symmetric(vertical: 10, horizontal: 30),
                  child: ListTile(
                    leading: Icon(Icons.phone,
                        size: 25,
                        color: Colors.teal
                    ),
                    title: Text('+12 345 678 900',
                    style: TextStyle(color: Colors.teal.shade900,
                    fontFamily: 'Montserrat',
                    fontSize: 17),
                    ),
                ),
              ),
              Card(
                color: Colors.white,
                margin: EdgeInsets.symmetric(vertical: 10, horizontal: 30),
                child: ListTile(
                  leading: Icon(Icons.email,
                        size: 25,
                        color: Colors.teal
                    ),
                  title: Text('tempcoffeeinthemorning.com',
                      style: TextStyle(color: Colors.teal.shade900,
                          fontFamily: 'Montserrat',
                          fontSize: 17),
                    ),
                ),
              ),
              Card(
                color: Colors.white,
                margin: EdgeInsets.symmetric(vertical: 10, horizontal: 30),
                  child: ListTile(
                    leading: Icon(Icons.home,
                        size: 25,
                        color: Colors.teal
                    ),
                    title: Text('123, Paddington Street',
                      style: TextStyle(
                      color: Colors.teal.shade900,
                      fontFamily: 'Montserrat',
                      fontSize: 17,
                    ),
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
