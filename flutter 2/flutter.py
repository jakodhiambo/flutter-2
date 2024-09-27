import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('My Dream App'),
          backgroundColor: Colors.blueAccent,
        ),
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              Text(
                'Welcome to My App!',
                style: TextStyle(fontSize: 24, color: Colors.purple),
              ),
              SizedBox(height: 20),
              ElevatedButton(
                onPressed: () {
                  print('Button Pressed!');
                },
                child: Text('Click Me'),
                style: ElevatedButton.styleFrom(primary: Colors.green),
              ),
            ],
          ),
        ),
      ),
    );
  }
}