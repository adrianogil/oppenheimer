import QtQuick 2.5
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.2

Rectangle {
    id: mainAppWindow

    width: 830
    height: 700

    visible: true
    color: "whitesmoke"

    anchors.verticalCenter: parent.verticalCenter
    anchors.horizontalCenter: parent.horizontalCenter

    Text {
        id: welcomeTitle
        text: qsTr("Canvas Board")
        font.bold: true
        font.pixelSize: 40

        // MouseArea to handle drag behavior
        MouseArea {
            id: dragArea

            anchors.fill: parent // Fill the area of the Text element

            property point lastMousePos

            onPressed: {
                lastMousePos = Qt.point(mouse.x, mouse.y)
            }

            onPositionChanged: {
                var mx = mouse.x
                var my = mouse.y
                var dx = mx - lastMousePos.x
                var dy = my - lastMousePos.y
                welcomeTitle.x += dx
                welcomeTitle.y += dy
                lastMousePos = Qt.point(mx, my)
            }
        }
    }
}