'use client'

import React, {useRef, useState} from 'react';
import {Input} from "@/components/ui/input"
import {Button} from "@/components/ui/button"
import api_domain from "../constants"

export default function MainPage() {
    const customRef = useRef("")
    const originalRef = useRef("")
    const [hideOriginalWarning, setHideOriginalWarning] = useState(true);
    const [hideCustomWarning, setHideCustomWarning] = useState(true);
    const [compressSuccess, setCompressSuccess] = useState(false);

    const [newUrl, setNewUrl] = useState("9a2cxa");
    const [copied, setCopied] = useState(false);

    const checkUrl = (strUrl) => {
        let expUrl = /^http[s]?:\/\/([\S]{3,})/i;
        return expUrl.test(strUrl);
    }

    const submit = () => {
        if (checkUrl(originalRef.current.value)) {
            setHideOriginalWarning(true)
        } else {
            setHideOriginalWarning(false)
            return
        }

        fetch(api_domain + "api/create", {
            method: "POST",
            mode:"cors",
            cache:"no-cache",
            credentials: "same-origin",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({"original_link": originalRef.current.value, "custom_link": customRef.current.value}),
        }).then((response) => response.json()).then((data) => {
            console.log(data)
            if (data["code"] === 1) {
                setCompressSuccess(true);
                setHideCustomWarning(true);

                setNewUrl(data["new_url"])
            } else {
                setCompressSuccess(false);
                setHideCustomWarning(false);
            }
        })


    }

    const copy = () => {
        navigator.clipboard.writeText("https://l2s.kro.kr/" + newUrl).then(() => {
            setCopied(true);
            setTimeout(() => {
                setCopied(false);
            }, 2000)
        })
    }

    return (
        (<main
            className="flex flex-col items-center justify-center h-screen bg-gradient-to-br from-indigo-500 to-purple-500">
            <div className="max-w-md w-full px-6 py-8 bg-white rounded-lg shadow-lg">
                <h1 className="text-4xl font-bold mb-4 text-center text-indigo-500">L2S</h1>
                <p className="text-gray-500 mb-6 text-center">Compress your links with ease.</p>
                <div className="space-y-4">
                    <div>
                        <label
                            className="block text-sm font-medium text-gray-700 mb-1"
                            htmlFor="original-link">
                            Original Link
                            <span className="text-red-500" id="original-link-warning" hidden={hideOriginalWarning}> -  Please enter a valid url</span>
                        </label>
                        <Input
                            className={!hideOriginalWarning ? "w-full border-2 border-red-500 focus:border-red-600 focus:ring-red-500" : "w-full border-2 border-indigo-500 focus:border-indigo-600 focus:ring-indigo-500"}
                            id="original-link"
                            placeholder="https://example.com"
                            type="url"
                            ref={originalRef}
                        />
                    </div>
                    <div>
                        <label
                            className="block text-sm font-medium text-gray-700 mb-1"
                            htmlFor="custom-link">
                            Custom Link (optional)
                            <span className="text-red-500" id="original-link-warning" hidden={hideCustomWarning}> -  Invalid url or already in use</span>
                        </label>
                        <div className="flex">
                            <span className={hideCustomWarning?"inline-flex items-center px-3 rounded-l-md border-2 border-r-0 border-indigo-500 bg-indigo-50 text-indigo-500":"inline-flex items-center px-3 rounded-l-md border-2 border-r-0 border-red-500 bg-red-50 text-red-500"}>
                            l2s.kro.kr/
                            </span>
                            <Input
                                className={hideCustomWarning ? "flex-1 rounded-l-none border-2 border-l-0 border-indigo-500 focus:border-indigo-600 focus:ring-indigo-500" : "flex-1 rounded-l-none border-2 border-l-0 border-red-500 focus:border-red-600 focus:ring-read-500"}
                                id="custom-link"
                                placeholder="your-custom-link"
                                type="text"
                                ref={customRef}
                            />
                        </div>
                    </div>
                    <div className="flex justify-between">
                        <Button
                            className="bg-indigo-100 text-indigo-500 hover:bg-indigo-200"
                            variant="secondary">
                            Clear
                        </Button>
                        <Button
                            className="bg-indigo-500 text-white hover:bg-indigo-600 focus:ring-indigo-500"
                            onClick={submit}>
                            Compress
                        </Button>
                    </div>
                </div>
                <div className="mt-6 text-center">
                    <p className="text-gray-500">{!compressSuccess?"Compressed link will be like:":"Your compessed link:"}</p>
                    <div
                        onClick={copy}
                        style={{ "cursor":"pointer" }}
                        className={!compressSuccess?"mt-2 bg-gradient-to-r from-indigo-100 to-purple-100 p-4 rounded-md":"mt-2 bg-gradient-to-r from-green-200 to-blue-100 p-4 rounded-md"}>
                        <p className="font-mono text-indigo-700">l2s.kro.kr/<span className="ex-short">{newUrl}</span></p>
                    </div>
                    <p className="p-1 text-gray-500 text-right" hidden={!copied}>
                        copied!
                    </p>
                </div>
            </div>
        </main>)
    );
}
