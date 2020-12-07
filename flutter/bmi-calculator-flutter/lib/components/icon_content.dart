import 'package:flutter/material.dart';
import 'package:bmi_calculator/constants.dart';
//write const for parameters up top so that can easily tweak later

class GenderCard extends StatelessWidget {
  //constructor
  GenderCard({this.text, this.icon});

  final String text;
  final IconData icon;

  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisAlignment: MainAxisAlignment.center,
      children: <Widget>[
        Icon(
          icon,
          size: 50.0,
        ),
        SizedBox(
          height: 15,
        ),
        Text(
          text,
          style: kLabelTextStyle,
        ),
      ],
    );
  }
}
