import React from 'react';
import Navbar from '../../components/Navbar';
import { accessCheck, roleCheck } from '../../utils/access_check';
import { useNavigate } from 'react-router-dom';

const LandingPage = () => {
    const navigate = useNavigate()
    const userid = localStorage.getItem('id')
    return (
        <div>
            {/* Navbar */}
            <Navbar />

            {/* Hero Section */}
            <section className="bg-gray-100 py-12">
                <div className="container mx-auto px-6 text-center">
                    <h2 className="text-3xl font-semibold text-gray-800 md:text-4xl">Learn with expert anytime anywhere</h2>
                    <p className="text-gray-600 mt-4">Our mission is to help people to find the best course online and learn with expert anytime, anywhere.</p>
                    {accessCheck() ?
                        <button className="mt-8 bg-blue-500 text-white px-8 py-3 rounded-md" onClick={() => { roleCheck() ? navigate(`/tutor/courses/${userid}`) : navigate(`/student/courses/${userid}`) }}>Go to Profile</button> :
                        <button className="mt-8 bg-blue-500 text-white px-8 py-3 rounded-md" onClick={() => { navigate(`/auth`) }}>Sign In / Sign Up</button>
                    }
                </div>
            </section>

            <section class="w-full bg-white pt-7 pb-7 md:pt-20 md:pb-24">
                <div class="box-border flex flex-col items-center content-center px-8 mx-auto leading-6 text-black border-0 border-gray-300 border-solid md:flex-row max-w-7xl lg:px-16">
                    <div class="box-border relative w-full max-w-md px-4 mt-5 mb-4 -ml-5 text-center bg-no-repeat bg-contain border-solid md:ml-0 md:mt-0 md:max-w-none lg:mb-0 md:w-1/2 xl:pl-10">
                        <img src="https://cdn.devdojo.com/images/december2020/productivity.png" class="p-2 pl-6 pr-5 xl:pl-16 xl:pr-20" />
                    </div>
                    <div class="box-border order-first w-full text-black border-solid md:w-1/2 md:pl-10 md:order-none">
                        <h2 class="m-0 text-xl font-semibold leading-tight border-0 border-gray-300 lg:text-3xl md:text-2xl">
                            Enhance Your Learning Experience
                        </h2>
                        <p class="pt-4 pb-8 m-0 leading-7 text-gray-700 border-0 border-gray-300 sm:pr-12 xl:pr-32 lg:text-lg">
                            VIDYA FLEX provides an engaging and effective online learning environment tailored to help you excel in your studies.
                        </p>
                        <ul class="p-0 m-0 leading-6 border-0 border-gray-300">
                            <li class="box-border relative py-1 pl-0 text-left text-gray-500 border-solid">
                                <span class="inline-flex items-center justify-center w-6 h-6 mr-2 text-white bg-yellow-300 rounded-full">
                                    <span class="text-sm font-bold">✓</span>
                                </span> Personalized learning paths for each student
                            </li>
                            <li class="box-border relative py-1 pl-0 text-left text-gray-500 border-solid">
                                <span class="inline-flex items-center justify-center w-6 h-6 mr-2 text-white bg-yellow-300 rounded-full">
                                    <span class="text-sm font-bold">✓</span>
                                </span> Experienced and qualified instructors
                            </li>
                            <li class="box-border relative py-1 pl-0 text-left text-gray-500 border-solid">
                                <span class="inline-flex items-center justify-center w-6 h-6 mr-2 text-white bg-yellow-300 rounded-full">
                                    <span class="text-sm font-bold">✓</span>
                                </span> Interactive and engaging lessons
                            </li>
                        </ul>
                    </div>
                </div>

                <div class="box-border flex flex-col items-center content-center px-8 mx-auto mt-2 leading-6 text-black border-0 border-gray-300 border-solid md:mt-20 xl:mt-0 md:flex-row max-w-7xl lg:px-16">
                    <div class="box-border w-full text-black border-solid md:w-1/2 md:pl-6 xl:pl-32">
                        <h2 class="m-0 text-xl font-semibold leading-tight border-0 border-gray-300 lg:text-3xl md:text-2xl">
                            Seamless Online Classes
                        </h2>
                        <p class="pt-4 pb-8 m-0 leading-7 text-gray-700 border-0 border-gray-300 sm:pr-10 lg:text-lg">
                            Join our live classes from anywhere, anytime. Experience the convenience of learning at your own pace with our flexible schedule.
                        </p>
                        <ul class="p-0 m-0 leading-6 border-0 border-gray-300">
                            <li class="box-border relative py-1 pl-0 text-left text-gray-500 border-solid">
                                <span class="inline-flex items-center justify-center w-6 h-6 mr-2 text-white bg-yellow-300 rounded-full">
                                    <span class="text-sm font-bold">✓</span>
                                </span> High-quality Mentorship
                            </li>
                            <li class="box-border relative py-1 pl-0 text-left text-gray-500 border-solid">
                                <span class="inline-flex items-center justify-center w-6 h-6 mr-2 text-white bg-yellow-300 rounded-full">
                                    <span class="text-sm font-bold">✓</span>
                                </span> Effiecint Learning
                            </li>
                            <li class="box-border relative py-1 pl-0 text-left text-gray-500 border-solid">
                                <span class="inline-flex items-center justify-center w-6 h-6 mr-2 text-white bg-yellow-300 rounded-full">
                                    <span class="text-sm font-bold">✓</span>
                                </span> Easy-to-use platform
                            </li>
                        </ul>
                    </div>

                    <div class="box-border relative w-full max-w-md px-4 mt-10 mb-4 text-center bg-no-repeat bg-contain border-solid md:mt-0 md:max-w-none lg:mb-0 md:w-1/2">
                        <img src="https://cdn.devdojo.com/images/december2020/settings.png" class="pl-4 sm:pr-10 xl:pl-10 lg:pr-32" />
                    </div>
                </div>
            </section>

            <section class="py-20 bg-gray-50">
                <div class="container items-center max-w-6xl px-4 px-10 mx-auto sm:px-20 md:px-32 lg:px-16">
                    <div class="flex flex-wrap items-center -mx-3">
                        <div class="order-1 w-full px-3 lg:w-1/2 lg:order-0">
                            <div class="w-full lg:max-w-md">
                                <h2 class="mb-4 text-3xl font-bold leading-tight tracking-tight sm:text-4xl font-heading">
                                    Comprehensive Learning Tools at Your Fingertips!
                                </h2>
                                <p class="mb-4 font-medium tracking-tight text-gray-400 xl:mb-6">
                                    VIDYA FLEX equips you with everything you need to excel in your studies. Our platform includes:
                                </p>
                                <ul>
                                    <li class="flex items-center py-2 space-x-4 xl:py-3">
                                        <svg class="w-8 h-8 text-pink-500" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 3v2m6-2v2M9 19v2m6-2v2M5 9H3m2 6H3m18-6h-2m2 6h-2M7 19h10a2 2 0 002-2V7a2 2 0 00-2-2H7a2 2 0 00-2 2v10a2 2 0 002 2zM9 9h6v6H9V9z"></path>
                                        </svg>
                                        <span class="font-medium text-gray-500">Interactive  Assignments</span>
                                    </li>
                                    <li class="flex items-center py-2 space-x-4 xl:py-3">
                                        <svg class="w-8 h-8 text-yellow-500" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"></path>
                                        </svg>
                                        <span class="font-medium text-gray-500">Comprehensive Learning</span>
                                    </li>
                                    <li class="flex items-center py-2 space-x-4 xl:py-3">
                                        <svg class="w-8 h-8 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path>
                                        </svg>
                                        <span class="font-medium text-gray-500">Secure and Private Communication Channels</span>
                                    </li>
                                </ul>
                            </div>
                        </div>
                        <div class="w-full px-3 mb-12 lg:w-1/2 lg:mb-0">
                            <img class="mx-auto sm:max-w-sm lg:max-w-full" src="https://cdn.devdojo.com/images/december2020/macbook.png" alt="feature image" />
                        </div>
                    </div>
                </div>
            </section>


            <section className="container mx-auto px-6 py-12">
                <h2 className="text-2xl font-semibold text-gray-800">Browse top category</h2>
                <div className="grid grid-cols-2 md:grid-cols-4 gap-6 mt-6">
                    {/* Sample Category */}
                    <div className="bg-white p-6 rounded-lg shadow">
                        <div className="text-lg font-medium text-gray-700">Development</div>
                        <div className="text-sm text-gray-500">42,089 Courses</div>
                    </div>

                    <div className="bg-white p-6 rounded-lg shadow">
                        <div className="text-lg font-medium text-gray-700">Tech</div>
                        <div className="text-sm text-gray-500">42,089 Courses</div>
                    </div>
                    <div className="bg-white p-6 rounded-lg shadow">
                        <div className="text-lg font-medium text-gray-700">Language</div>
                        <div className="text-sm text-gray-500">42,089 Courses</div>
                    </div>
                    {/* Repeat for other categories */}
                </div>
            </section>

            {/* Best Selling Courses */}
            <section className="bg-gray-100 py-12">
                <div className="container mx-auto px-6">
                    <h2 className="text-2xl font-semibold text-gray-800">Best selling courses</h2>
                    <div className="grid grid-cols-2 md:grid-cols-4 gap-6 mt-6">
                        {/* Sample Course Card */}
                        <div className="bg-white p-6 rounded-lg shadow">
                            <img src="course-image.jpg" alt="Course" className="w-full h-32 object-cover rounded-md" />
                            <h3 className="text-lg font-medium text-gray-700 mt-4">Course Title</h3>
                            <p className="text-sm text-gray-500">Instructor Name</p>
                            <div className="flex justify-between items-center mt-4">
                                <span className="text-xl font-bold text-gray-800">$57</span>
                                <button className="text-blue-500 hover:underline">Enroll</button>
                            </div>
                        </div>
                        {/* Repeat for other courses */}
                    </div>
                </div>
            </section>

            {/* Footer */}
            <footer className="bg-gray-800 text-white py-12">
                <div className="container mx-auto px-6">
                    <div className="flex justify-between">
                        <div>
                            <h3 className="text-lg font-semibold">E-tutor</h3>
                            <p className="text-sm">A description of your platform can go here.</p>
                        </div>
                        <div>
                            <h3 className="text-lg font-semibold">Company</h3>
                            <nav className="mt-4 space-y-2">
                                <a href="#" className="text-gray-400 hover:text-white">About Us</a>
                                <a href="#" className="text-gray-400 hover:text-white">Contact</a>
                                <a href="#" className="text-gray-400 hover:text-white">Support</a>
                            </nav>
                        </div>
                        <div>
                            <h3 className="text-lg font-semibold">Support</h3>
                            <nav className="mt-4 space-y-2">
                                <a href="#" className="text-gray-400 hover:text-white">FAQs</a>
                                <a href="#" className="text-gray-400 hover:text-white">Help Center</a>
                            </nav>
                        </div>
                    </div>
                </div>
            </footer>
        </div>
    );
};

export default LandingPage;
