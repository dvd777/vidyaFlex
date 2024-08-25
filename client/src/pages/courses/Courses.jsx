import React, { useEffect, useState } from 'react';
import Navbar from '../../components/Navbar';
import axios from 'axios';
import config from '../../config';
import courseimage from '../../assets/course.webp'
import { Link } from 'react-router-dom';



const Courses = () => {
    const [courses, setCourses] = useState([]);

    useEffect(() => {
        const fetchCourses = async () => {
            try {
                const response = await axios.get(`${config.base_url}/courses/`);
                setCourses(response.data);
            } catch (error) {
                console.error('Failed to fetch courses:', error);
            }
        };

        fetchCourses();
    }, []);

    return (
        <div>
            {/* Navbar */}
            <Navbar />


            {/* Course List */}
            <section className="container mx-auto px-6 py-12">
                <div className="flex justify-between items-center mb-4">
                    <h2 className="text-2xl font-semibold text-gray-800">Courses</h2>
                    {/* <div className="flex items-center">
                        <button className="bg-gray-200 text-gray-800 px-4 py-2 rounded-md mr-4">Filter</button>
                        <input type="text" placeholder="Search..." className="border border-gray-300 px-4 py-2 rounded-md" />
                    </div> */}
                </div>
                <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
                    {courses.map(course => (
                        <Link key={course.id} className="bg-white p-4 rounded-lg shadow" to={`/courses/${course.id}`}>
                            <img src={config.base_url + course.course_profile || courseimage} alt={course.course_name} className="w-full h-32 object-cover rounded-md" />
                            <div className="mt-4">
                                <h3 className="text-lg font-medium text-gray-800">{course.course_name}</h3>
                                <p className="text-sm text-gray-500">{course.course_description}</p>
                                <div className="flex justify-between items-center mt-2">
                                    <span className="text-xl font-bold text-gray-800">{course.course_price ? `$${course.course_price}` : 'Free'}</span>
                                    <span className="text-gray-600">{course.course_rating ? `${course.course_rating}★` : 'No ratings'}</span>
                                </div>
                                <p className="text-sm text-gray-600 mt-2">{course.students.length} students</p>
                            </div>
                        </Link>
                    ))}
                </div>
            </section>

            {/* Pagination */}


            {/* Footer */}
            <footer className="bg-gray-800 text-white py-12 mt-12">
                <div className="container mx-auto px-6">
                    <div className="grid grid-cols-2 md:grid-cols-4 gap-6">
                        <div>
                            <h3 className="text-lg font-semibold">E-tutor</h3>
                            <p className="text-sm">A description of your platform can go here.</p>
                        </div>
                        <div>
                            <h3 className="text-lg font-semibold">Top Categories</h3>
                            <nav className="mt-4 space-y-2">
                                <a href="#" className="text-gray-400 hover:text-white">Development</a>
                                <a href="#" className="text-gray-400 hover:text-white">Finance & Accounting</a>
                                <a href="#" className="text-gray-400 hover:text-white">Design</a>
                                <a href="#" className="text-gray-400 hover:text-white">Business</a>
                            </nav>
                        </div>
                        <div>
                            <h3 className="text-lg font-semibold">Quick Links</h3>
                            <nav className="mt-4 space-y-2">
                                <a href="#" className="text-gray-400 hover:text-white">Become Instructor</a>
                                <a href="#" className="text-gray-400 hover:text-white">Contact</a>
                                <a href="#" className="text-gray-400 hover:text-white">Career</a>
                            </nav>
                        </div>
                        <div>
                            <h3 className="text-lg font-semibold">Support</h3>
                            <nav className="mt-4 space-y-2">
                                <a href="#" className="text-gray-400 hover:text-white">Help Center</a>
                                <a href="#" className="text-gray-400 hover:text-white">Terms & Conditions</a>
                                <a href="#" className="text-gray-400 hover:text-white">Privacy Policy</a>
                            </nav>
                        </div>
                    </div>
                </div>
            </footer>
        </div>
    );
};

export default Courses;
