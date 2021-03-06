package com.example.eyetracking;

import android.accessibilityservice.AccessibilityService;
import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.hardware.camera2.CameraAccessException;
import android.hardware.camera2.CameraCharacteristics;
import android.hardware.camera2.CameraManager;
import android.hardware.camera2.CaptureRequest;
import android.media.FaceDetector;
import android.provider.MediaStore;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.SurfaceView;
import android.view.View;
import android.view.WindowManager;
import android.widget.Button;

import org.opencv.android.BaseLoaderCallback;
import org.opencv.android.CameraBridgeViewBase;
import org.opencv.android.JavaCamera2View;
import org.opencv.android.JavaCameraView;
import org.opencv.android.LoaderCallbackInterface;
import org.opencv.android.OpenCVLoader;
import org.opencv.core.Core;
import org.opencv.core.CvType;
import org.opencv.core.Mat;
import org.opencv.core.MatOfRect;
import org.opencv.core.Rect;
import org.opencv.core.Scalar;
import org.opencv.core.Size;
import org.opencv.imgproc.Imgproc;
import org.opencv.objdetect.CascadeClassifier;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;

public class MainActivity extends AppCompatActivity implements CameraBridgeViewBase.CvCameraViewListener {

    private static String originID = "MainActivity";
    private CameraBridgeViewBase openCvCameraView;
    private CascadeClassifier cascadeClassifier;
    private Mat newimage;
    private int absoluteFaceSize;
    private int absoluteEyeSize;
    private int ffcameraid;
    Mat mat;

    BaseLoaderCallback mLoaderCallBack = new BaseLoaderCallback(this) {
        @Override
        public void onManagerConnected(int status) {
            switch (status){
                case BaseLoaderCallback.SUCCESS:{
                    initializeOpenCVDependencies();
                    break;
                }
                default:{
                    super.onManagerConnected(status);
                    break;
                }
            }
            super.onManagerConnected(status);
        }
    };

    static {
        if (OpenCVLoader.initDebug()){
            Log.i(originID, "OpenCV executed successfully." );

        }
        else {
            Log.i(originID, "OpenCV failed.");
        }
    }


    @Override
    protected void onCreate(Bundle savedInstanceState) {        // initializes camera for viewing
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        getWindow().addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON);
        openCvCameraView = findViewById(R.id.java_camera2_view);
        openCvCameraView.setCameraIndex(CameraBridgeViewBase.CAMERA_ID_FRONT);
        openCvCameraView.setCvCameraViewListener(this);
    }

    

    @Override
    protected void onPause(){
        super.onPause();
        if (openCvCameraView != null) {
            openCvCameraView.disableView();
        }
    }
    @Override
    protected void onDestroy(){
        super.onDestroy();
        if(openCvCameraView != null){
            openCvCameraView.disableView();
        }
    }

    private void initializeOpenCVDependencies(){
        try {
            InputStream is = getResources().openRawResource(R.raw.haarcascade_eye);
            File cascadeDir = getDir("cascade", Context.MODE_APPEND);
            File mCascadeFile = new File(cascadeDir, "haarcascade_eye.xml");
            FileOutputStream os = new FileOutputStream(mCascadeFile);
            byte[] buffer = new byte[4096];
            int bytesRead;
            while ((bytesRead = is.read(buffer)) != -1) {
                os.write(buffer, 0, bytesRead);
            }
            is.close();
            os.close();
            cascadeClassifier = new CascadeClassifier(mCascadeFile.getAbsolutePath());
        }
        catch (Exception e){
            Log.e("OpenCVActivity", "Error loading cascade", e);
        }
        openCvCameraView.enableView();
    }

    @Override
    protected void onResume(){
        super.onResume();
        if(OpenCVLoader.initDebug()){
            Log.i(originID, "OpenCV executed successfully.");
            mLoaderCallBack.onManagerConnected(LoaderCallbackInterface.SUCCESS);
        }
        else {
            Log.i(originID, "OpenCV failed.");
            OpenCVLoader.initAsync(OpenCVLoader.OPENCV_VERSION_2_4_9, this, mLoaderCallBack);
        }
    }

    @Override
    public void onCameraViewStarted(int width, int height) {
        newimage = new Mat(height, width, CvType.CV_8UC4);
        absoluteFaceSize = (int) (height * 0.2);
        absoluteEyeSize = (int) (height * 0.04);
    }

    @Override
    public void onCameraViewStopped() {
        mat.release();
    }

    @Override
    public Mat onCameraFrame(Mat inputFrame) {
        Core.flip(inputFrame,inputFrame,-1);                        // flips the camera to be upright, but not mirrored
        Imgproc.cvtColor(inputFrame, newimage, Imgproc.COLOR_RGB2BGR);      // fixes blue screen
        MatOfRect faces = new MatOfRect();
        Mat eye = new Mat();
        MatOfRect eyes = new MatOfRect();
        if (cascadeClassifier != null) {                // detect faces with classifier
            cascadeClassifier.detectMultiScale(newimage, faces, 1.1, 2, 2,
                    new Size(absoluteFaceSize, absoluteFaceSize), new Size());
        }
        Rect[] facesArray = faces.toArray();
        Rect[] eyesArray = eyes.toArray();
        for (int i = 0; i < facesArray.length; i++) {   // draw rectangle around detected faces
            Imgproc.rectangle(inputFrame, facesArray[i].tl(), facesArray[i].br(), new Scalar(0, 255, 0, 255), 3);

        /*
            //cascadeClassifier.detectMultiScale(eye, eyes, 1.1, 2, 0, new Size( 30, 30), new Size());
            cascadeClassifier.detectMultiScale(newimage, eyes, 1.1, 2, 2, new Size(absoluteEyeSize, absoluteEyeSize), new Size());

            for (int j = 0; j < eyesArray.length; j++) {
                Imgproc.rectangle(inputFrame, eyesArray[i].tl(), eyesArray[i].br(), new Scalar(0, 255, 0, 255), 1);
            }

        */
        }
        return inputFrame;
    }

}
